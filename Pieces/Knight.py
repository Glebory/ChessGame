from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Knight(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackKnightImage = ImageTk.PhotoImage(file="images/knight1.png")
        self.DEFAULTWhiteKnightImage = ImageTk.PhotoImage(file="images/knight.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        knight_moves = []
        for i, j in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                if self.color == "white":
                    white_moves = [(i-2, j-1), (i-2, j+1), (i-1, j+2), (j-2, i-1)]
                    knight_moves += white_moves
                else:
                    black_moves = [(i+2, j-1), (i+2, j+1), (i+1, j+2), (i+1, j-2)]
                    knight_moves += black_moves
        return knight_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackKnightImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteKnightImage
        return self.image
