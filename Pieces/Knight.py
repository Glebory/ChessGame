from PIL import ImageTK
class Knight:
    def __init__(self, color, board, position):
        GameObjects.__init__(color, board, position)
        self.whiteKnightMoves = []
        self.blackKnightMoves = []
        self.DEFAULTblackKnightImage = ImageTk.PhotoImage(file="images/knight1.png")
        self.DEFAULTwhiteKnightImage = ImageTk.PhotoImage(file="images/knight.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        for x in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                if self.color = "white":
                    whiteMoves = [(i-2, j-1), (i-2, j+1), (i-1, j+2), (j-2, i-1)]
                    self.whiteKnightMoves += whiteMoves
                else:
                    blackMoves = [(i+2, j-1), (i+2, j+1), (i+1, j+2), (i+1, j-2)]
                    self.blackKnightMoves += blackMoves

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackKnightImage
        elif self.color = "white":
            image = self.DEFAULTwhiteKnightImage
        return image
