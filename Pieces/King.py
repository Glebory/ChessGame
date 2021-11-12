from PIL import ImageTk
from Chessticles.Pieces import GameObjects


class King(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.KingMoves = []
        self.DEFAULTBlackKingImage = ImageTk.PhotoImage(file="Pieces/images/king1.png")
        self.DEFAULTWhiteKingImage = ImageTk.PhotoImage(file="Pieces/images/king.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        for i, j in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                possible_moves = [(i+1, j-1), (i+1, j), (i+1, j+1), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j), (i-1, j+1)]
                self.KingMoves += possible_moves

    def initialize_image(self):
        if self.color == "black":
            self._image = self.DEFAULTBlackKingImage
        elif self.color == "white":
            self._image = self.DEFAULTWhiteKingImage

