from PIL import ImageTK
class King:
    def __init__(self, color, board, position):
        GameObjects.__init__(color, board, position)
        self.KingMoves = []
        self.DEFAULTblackKingImage = ImageTk.PhotoImage(file="images/king1.png")
        self.DEFAULTwhiteKingImage = ImageTk.PhotoImage(file="images/king.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        for x in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                possibleMoves = [(i+1, j-1), (i+1, j), (i+1, j+1), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j), (i-1, j+1)]
            self.KingMoves += possibleMoves

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackKingImage
        elif self.color = "white":
            image = self.DEFAULTwhiteKingImage
        return image
