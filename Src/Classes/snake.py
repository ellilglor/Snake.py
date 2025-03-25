class Snake(object):
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def head(self):
        return self.body[-1]

    def takeStep(self, position):
        self.body = self.body[1:1] + [position]

    def extend_body(self, position):
        self.body.append(position)

    def set_direction(self, direction):
        self.direction = direction