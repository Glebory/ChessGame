from PIL import ImageTk
from Chessticles.Pieces import GameObjects


class Bishop(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.bishopMoves = []
        self.DEFAULTBlackBishopImage = ImageTk.PhotoImage(file="Pieces/images/bishop1.png")
        self.DEFAULTWhiteBishopImage = ImageTk.PhotoImage(file="Pieces/images/bishop.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        # check within bounds of board
        for x in range(1, 8):
            for i, j in range(1, 8):
                possible_moves = [(i-x, j-x), (i+x, j+x)]
                self.bishopMoves += possible_moves

    def initialize_image(self):
        if self.color == "black":
            self._image = self.DEFAULTBlackBishopImage
        elif self.color == "white":
            self._image = self.DEFAULTWhiteBishopImage


