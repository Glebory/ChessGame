from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Pawn(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.DEFAULTBlackPawnImage = ImageTk.PhotoImage(file="images/pawn1.png")
        self.DEFAULTWhitePawnImage = ImageTk.PhotoImage(file="images/pawn.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        pawn_moves = []
        for i, j in range(1, 8):
            if self.color == "white":
                if self.board[i] == 6 and self.color == "white":
                    possible_moves = [(i-2, j), (i-1, j)]
                    pawn_moves += possible_moves
                else:
                    pawn_moves += (i-1, j)
            else:
                if self.board[i] == 1 and self.color == "black":
                    possible_moves = [(i+2, j), (i+1, j)]
                    pawn_moves += possible_moves
                else:
                    pawn_moves += (i+1, j)
        return pawn_moves

    def initialize_image(self):
        if self.color == "black":
            self.image = self.DEFAULTBlackPawnImage
        elif self.color == "white":
            self.image = self.DEFAULTWhitePawnImage
        return self.image
