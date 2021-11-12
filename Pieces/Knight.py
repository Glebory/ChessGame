from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Knight(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackKnightImage = ImageTk.PhotoImage(file="Pieces/images/knight1.png")
        self.DEFAULTWhiteKnightImage = ImageTk.PhotoImage(file="Pieces/images/knight.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        knight_moves = []
        two = [2, -2]
        one = [1, -1]
        for i in two:
            for j in one:
                if self.position[0] + i in range(8) and self.position[1] + j in range(8):
                    knight_moves += [(self.position[0] + i, self.position[1] + j)]
                if self.position[1] + i in range(8) and self.position[0] + j in range(8):
                    knight_moves += [(self.position[0] + j, self.position[1] + i)]
        return knight_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackKnightImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteKnightImage
        return self.image
