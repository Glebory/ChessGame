class Queen:
    def __init__(self, color, board):
        GameObjects.__init__(color, board)
        self.whiteQueenMoves = []
        self.blackQueenMoves = []

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        if 0 <= i <= 7 and 0 <= j <= 7:
            if self.color == "white":
                whiteMoves = [(i - x, j), (i + x, j), (i, j - x), (i, j + x), (i-x, j-x), (i+x, j+x)]
                self.whiteQueenMoves += whiteMoves
            else:
                blackMoves = [(i + x, j), (i - x, j), (i, j + x), (i, j - x), (i-x, j-x), (i+x, j+x)]
                self.blackQueenMoves += blackMoves
