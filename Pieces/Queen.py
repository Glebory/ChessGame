from PIL import ImageTK
class Queen(GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whiteQueenMoves = []
        self.blackQueenMoves = []
        self.DEFAULTblackQueenImage = ImageTk.PhotoImage(file="images/queen1.png")
        self.DEFAULTwhiteQueenImage = ImageTk.PhotoImage(file="images/queen.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        for i in range(1,8):
            for j in range(1,8):
                if self.color == "white":
                    whiteMoves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x), (i-x, j-x), (i+x, j+x)]
                    self.whiteQueenMoves += whiteMoves
                else:
                    blackMoves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x), (i-x, j-x), (i+x, j+x)]
                    self.blackQueenMoves += blackMoves


    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackQueenImage
        elif self.color = "white":
            image = self.DEFAULTwhiteQueenImage
        return image
