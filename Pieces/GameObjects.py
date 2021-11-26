class GameObjects:
    def __init__(self, color, board, position):
        self.color = color
        self.board = board
        self._position = position
        self._image = ""

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, new_image):
        self._image = new_image

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self.position = new_position

    def initialize_image(self):
        pass
