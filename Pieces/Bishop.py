from PIL import ImageTK
from Chessticles.Pieces import GameObjects


class Bishop(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.bishopMoves = []
        self.DEFAULTBlackBishopImage = ImageTK.PhotoImage(file="images/bishop1.png")
        self.DEFAULTWhiteBishopImage = ImageTK.PhotoImage(file="images/bishop.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        # check within bounds of board
        for x in range(1, 8):
            for i, j in range(1, 8):
                possible_moves = [(i-x, j-x), (i+x, j+x)]
                self.bishopMoves += possible_moves

    def initialize_image(self):
        if self.color == "black":
            image = self.DEFAULTBlackBishopImage
        elif self.color == "white":
            image = self.DEFAULTWhiteBishopImage
        return image
