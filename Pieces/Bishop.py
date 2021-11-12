from PIL import ImageTk
from Chessticles.Pieces import GameObjects


class Bishop(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackBishopImage = ImageTk.PhotoImage(file="images/bishop1.png")
        self.DEFAULTWhiteBishopImage = ImageTk.PhotoImage(file="images/bishop.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        # check within bounds of board
        bishop_moves = []
        for x in range(1, 7):
            if self.position[0] + x <= 7 and self.position[1] + x <= 7:
                bishop_moves += [(self.position[0] + x, self.position[1] + x)]
            if self.position[0] - x >= 0 and self.position[1] - x >= 0:
                bishop_moves += [(self.position[0] - x, self.position[1] - x)]
            if self.position[0] - x >= 0 and self.position[1] + x <= 7:
                bishop_moves += [(self.position[0] - x, self.position[1] + x)]
            if self.position[0] + x <= 7 and self.position[1] - x >= 0:
                bishop_moves += [(self.position[0] + x, self.position[1] - x)]

        return bishop_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackBishopImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteBishopImage
        return self.image
