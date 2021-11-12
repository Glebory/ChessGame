from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Queen(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackQueenImage = ImageTk.PhotoImage(file="Pieces/images/queen1.png")
        self.DEFAULTWhiteQueenImage = ImageTk.PhotoImage(file="Pieces/images/queen.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        queen_moves = []
        for x in range(1, 8):
            if self.position[0] + x <= 7 and self.position[1] + x <= 7:
                queen_moves += [(self.position[0] + x, self.position[1] + x)]
            if self.position[0] - x >= 0 and self.position[1] - x >= 0:
                queen_moves += [(self.position[0] - x, self.position[1] - x)]
            if self.position[0] - x >= 0 and self.position[1] + x <= 7:
                queen_moves += [(self.position[0] - x, self.position[1] + x)]
            if self.position[0] + x <= 7 and self.position[1] - x >= 0:
                queen_moves += [(self.position[0] + x, self.position[1] - x)]
            if self.position[0] - x >= 0:
                queen_moves += [(self.position[0] - x, self.position[1])]
            if self.position[0] + x <= 7:
                queen_moves += [(self.position[0] + x, self.position[1])]
            if self.position[1] - x >= 0:
                queen_moves += [(self.position[0], self.position[1] - x)]
            if self.position[1] + x <= 7:
                queen_moves += [(self.position[0], self.position[1] + x)]

        return queen_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackQueenImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteQueenImage
        return self.image

