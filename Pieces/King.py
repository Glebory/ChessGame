from PIL import ImageTk
from Chessticles.Pieces import GameObjects


class King(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackKingImage = ImageTk.PhotoImage(file="images/king1.png")
        self.DEFAULTWhiteKingImage = ImageTk.PhotoImage(file="images/king.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        king_moves = []
        for i, j in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                possible_moves = [(i+1, j-1), (i+1, j), (i+1, j+1), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j), (i-1, j+1)]
                king_moves += possible_moves
        return king_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackKingImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteKingImage
        return self.image
