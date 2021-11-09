class Bishop:
    def __init__(self, color, board):
        GameObjects.__init__(color, board)
        self.bishopMoves = []

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def checkValidMoves(self):
        # check within bounds of board
        if 0 <= i <= 7 and 0 <= j <= 7:
            for x in range(1,8):
                possibleMoves = [(i-x, j-x), (i+x, j+x)]
                self.bishopMoves += possibleMoves
