from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Rook(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whiteRookMoves = []
        self.blackRookMoves = []
        self.DEFAULTBlackRookImage = ImageTk.PhotoImage(file="images/rook1.png")
        self.DEFAULTWhiteRookImage = ImageTk.PhotoImage(file="images/rook.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        # check if within bounds of board
        for x in range(1, 8):
            for i, j in range(1, 8):
                if 0 <= i <= 7 and 0 <= j <= 7:
                    if self.color == "white":
                        white_moves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x)]
                        self.whiteRookMoves += white_moves
                    else:
                        black_moves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x)]
                        self.blackRookMoves += black_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackRookImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteRookImage
        return self.image
