from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Queen(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whiteQueenMoves = []
        self.blackQueenMoves = []
        self.DEFAULTBlackQueenImage = ImageTk.PhotoImage(file="images/queen1.png")
        self.DEFAULTWhiteQueenImage = ImageTk.PhotoImage(file="images/queen.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        for x in range(1,8):
            for i, j in range(1, 8):
                if self.color == "white":
                    white_moves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x), (i-x, j-x), (i+x, j+x)]
                    self.whiteQueenMoves += white_moves
                else:
                    black_moves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x), (i-x, j-x), (i+x, j+x)]
                    self.blackQueenMoves += black_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackQueenImage
        elif self.color == "white":
            self.image = self.DEFAULTWhiteQueenImage
        return self.image
