class GameObjects:
    def __init__(self, color: str, board, position):
        self.color = color
        self.board = board
        self.position = position
        self.image = self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, new_image):
        self.image = new_image

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, new_position):
        self.position = new_position
