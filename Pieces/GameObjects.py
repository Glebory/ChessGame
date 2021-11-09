class GameObjects:
    def __init__(self, color: str, board):
        self.color = color
        self.board = board

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, pieceColor):
        self.color = pieceColor

    def move(self, board):
