class King:
    def __init__(self, color, board):
        GameObjects.__init__(color, board)
        self.KingMoves = []

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        for x in range(1, 8):
            # check if within bounds of board
            if 0 <= i <= 7 and 0 <= j <= 7:
                possibleMoves = [(i+1, j-1), (i+1, j), (i+1, j+1), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j), (i-1, j+1)]
            self.KingMoves += possibleMoves
