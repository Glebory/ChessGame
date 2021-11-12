from PIL import ImageTK
class Bishop(GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.bishopMoves = []
        self.DEFAULTblackBishopImage = ImageTk.PhotoImage(file="images/bishop1.png")
        self.DEFAULTwhiteBishopImage = ImageTk.PhotoImage(file="images/bishop.png")

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        # check within bounds of board
        for i in range(1,8):
            for j in range(1,8):
                for x in range(1,8):
                    possibleMoves = [(i-x, j-x), (i+x, j+x)]
                    self.bishopMoves += possibleMoves

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackBishopImage
        elif self.color = "white":
            image = self.DEFAULTwhiteBishopImage
        return image
