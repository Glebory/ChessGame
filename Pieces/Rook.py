from PIL import ImageTK
class Rook(GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whiteRookMoves = []
        self.blackRookMoves = []
        self.DEFAULTblackRookImage = ImageTk.PhotoImage(file="images/rook1.png")
        self.DEFAULTwhiteRookImage = ImageTk.PhotoImage(file="images/rook.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
            # check if within bounds of board
            for i in range(1,8):
                for j in range(1,8):
                    if 0 <= i <= 7 and 0 <= j <= 7:
                        if self.color == "white":
                            whiteMoves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x)]
                            self.whiteRookMoves += whiteMoves
                        else:
                            blackMoves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x)]
                            self.blackRookMoves += blackMoves

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackRookImage
        elif self.color = "white":
            image = self.DEFAULTwhiteRookImage
        return image
