class Snake(object):
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def head(self):
        return self.body[-1]

    def takeStep(self, position):
        self.body.pop(0)
        self.body.append(position)

    def extendBody(self, position):
        self.body.append(position)

    def setDirection(self, direction):
        self.direction = direction