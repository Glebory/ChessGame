from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Pawn(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackPawnImage = ImageTk.PhotoImage(file="images/pawn1.png")
        self.DEFAULTWhitePawnImage = ImageTk.PhotoImage(file="images/pawn.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        pawn_moves = []
        for y in range(1, 3):
            pawn_moves += [(self.position[0], self.position[1] + y)]
        return pawn_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackPawnImage
        elif self.color == "white":
            self.image = self.DEFAULTWhitePawnImage
        return self.image

