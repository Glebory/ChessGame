import GameObjects
class Pawn:
    def __init__(self, color, board):
        GameObjects.__init__(color, board)
        self.whitePawnMoves = []
        self.blackPawnMoves = []

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
