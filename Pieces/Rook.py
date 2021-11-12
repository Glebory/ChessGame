from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Rook(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackRookImage = ImageTk.PhotoImage(file="images/rook1.png")
        self.DEFAULTWhiteRookImage = ImageTk.PhotoImage(file="images/rook.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        rook_moves = []
        for x in range(1, 8):
            if self.position[0] - x >= 0:
                rook_moves += [(self.position[0] - x, self.position[1])]
            if self.position[0] + x <= 7:
                rook_moves += [(self.position[0] + x, self.position[1])]
            if self.position[1] - x >= 0:
                rook_moves += [(self.position[0], self.position[1] - x)]
            if self.position[1] + x <= 7:
                rook_moves += [(self.position[0], self.position[1] + x)]
        return rook_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackRookImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteRookImage
        return self.image

