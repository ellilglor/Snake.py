import Classes.snake as snake

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

    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.snake = snake.Snake([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], self.UP)

    def __buildBoard(self):
        board = [[self.EMPTY for _ in range(self.height)] for _ in range(self.width)]

        for part in self.snake.body:
            board[part[0]][part[1]] = self.BODY

        head = self.snake.head()
        board[head[0]][head[1]] = self.HEAD

        return board

    def renderBoard(self):
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

