from PIL import ImageTK
class Bishop:
    def __init__(self, color, board, position):
        GameObjects.__init__(color, board, position)
        self.bishopMoves = []
        self.DEFAULTblackBishopImage = ImageTk.PhotoImage(file="images/bishop1.png")
        self.DEFAULTwhiteBishopImage = ImageTk.PhotoImage(file="images/bishop.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        # check within bounds of board
        if 0 <= i <= 7 and 0 <= j <= 7:
            for x in range(1,8):
                possibleMoves = [(i-x, j-x), (i+x, j+x)]
                self.bishopMoves += possibleMoves

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackBishopImage
        elif self.color = "white":
            image = self.DEFAULTwhiteBishopImage
        return image
