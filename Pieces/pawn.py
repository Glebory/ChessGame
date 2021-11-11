from PIL import ImageTK
class Pawn:
    def __init__(self, color, board, position):
        GameObjects.__init__(color, board, position)
        self.whitePawnMoves = []
        self.blackPawnMoves = []
        self.DEFAULTblackPawnImage = ImageTk.PhotoImage(file="images/pawn1.png")
        self.DEFAULTwhitePawnImage = ImageTk.PhotoImage(file="images/pawn.png")

    def __str__():
        return "%s %s" % (self.color, self.position)

    def checkValidWhiteMoves(self):
            if self.color == "white":
                if self.board[i] == 6 and self.color = "white":
                    self.whitePawnMoves.append([i-2][j])
                else:
                    self.whitePawnMoves.append([i-1][j])
            else:
                if self.board[i] == 1 and self.color = "black":
                    self.blackPawnMoves.append([i+2][j])
                else:
                    self.blackPawnMoves.append([i+1][j])

    def initialize_image():
        if self.color = "black":
            image = self.DEFAULTblackPawnImage
        elif self.color = "white":
            image = self.DEFAULTwhitePawnImage
        return image
