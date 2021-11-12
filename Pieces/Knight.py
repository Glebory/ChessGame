from Chessticles.Pieces import GameObjects
from PIL import ImageTK


class Knight(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whiteKnightMoves = []
        self.blackKnightMoves = []
        self.DEFAULTBlackKnightImage = ImageTK.PhotoImage(file="images/knight1.png")
        self.DEFAULTWhiteKnightImage = ImageTK.PhotoImage(file="images/knight.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        for i, j in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                if self.color == "white":
                    white_moves = [(i-2, j-1), (i-2, j+1), (i-1, j+2), (j-2, i-1)]
                    self.whiteKnightMoves += white_moves
                else:
                    black_moves = [(i+2, j-1), (i+2, j+1), (i+1, j+2), (i+1, j-2)]
                    self.blackKnightMoves += black_moves

    def initialize_image(self):
        if self.color == "black":
            image = self.DEFAULTBlackKnightImage
        elif self.color == "white":
            image = self.DEFAULTWhiteKnightImage
        return image
