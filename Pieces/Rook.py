class Rook:
    def __init__(self, color, board):
        GameObjects.__init__(color, board)
        self.whiteRookMoves = []
        self.blackRookMoves = []

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                if self.color == "white":
                    whiteMoves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x)]
                    self.whiteRookMoves += whiteMoves
                else:
                    blackMoves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x)]
                    self.blackRookMoves += blackMoves
