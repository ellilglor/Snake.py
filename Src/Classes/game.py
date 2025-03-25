import random
import Classes.snake as snake
import Classes.apple as apple

class Game(object):
    EMPTY = 0
    BODY = 1
    HEAD = 2
    APPLE = 3

    DISPLAY_CHARS = {
        EMPTY: " ",
        BODY: "O",
        HEAD: "X",
        APPLE: "*",
    }

    UP = (0,1)
    DOWN = (0,-1)
    LEFT = (-1,0)
    RIGHT = (1,0)

    INPUT_UP = "W"
    INPUT_DOWN = "S"
    INPUT_LEFT = "A"
    INPUT_RIGHT = "D"
    INPUT_END = "E"

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.score = 0
        self.snake = snake.Snake([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], self.UP)
    
    def play(self):
        self.__generateApple()

        while (True):
            self.__renderBoard()

            char = input().upper()

            if char == self.INPUT_UP and self.snake.direction != self.DOWN:
                self.snake.setDirection(self.UP)
            elif char == self.INPUT_DOWN and self.snake.direction != self.UP:
                self.snake.setDirection(self.DOWN)
            elif char == self.INPUT_LEFT and self.snake.direction != self.RIGHT:
                self.snake.setDirection(self.LEFT)
            elif char == self.INPUT_RIGHT and self.snake.direction != self.LEFT:
                self.snake.setDirection(self.RIGHT)
            elif char == self.INPUT_END:
                break

            next_position = self.__nextPosition(self.snake.head(), self.snake.direction)
            if next_position in self.snake.body:
                break

            if next_position == self.apple.location:
                self.score += self.apple.points
                self.snake.extendBody(next_position)
                self.__generateApple()
            else:
                self.snake.takeStep(next_position)

        self.__finishGame()
        
    def __finishGame(self):
        print(f"You finished with a score of {self.score}.")

    def __buildBoard(self):
        board = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]

        for part in self.snake.body:
            board[part[0]][part[1]] = self.BODY

        head = self.snake.head()
        board[head[0]][head[1]] = self.HEAD

        board[self.apple.location[0]][self.apple.location[1]] = self.APPLE

        return board
    
    def __generateApple(self):
        while (True):
            location = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if (location not in self.snake.body):
                break
        
        points = 1
        self.apple = apple.Apple(location, points)
    
    def __nextPosition(self, position, step):
        return ((position[0] + step[0]) % self.width, (position[1] + step[1]) % self.height)

    def __renderBoard(self):
        board = self.__buildBoard()
        horizontalBorder = "+" + "-" * self.width + "+"
        verticalBorder = "|"

        print(horizontalBorder)

        for i in range(self.height):
            row = verticalBorder
            for j in range(self.width):
                value = board[j][self.height - 1 - i]
                row += self.DISPLAY_CHARS[value]
            row += verticalBorder
            print (row)

        print(horizontalBorder)
