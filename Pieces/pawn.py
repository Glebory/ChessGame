from Chessticles.Pieces import GameObjects
from PIL import ImageTk


class Pawn(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.whitePawnMoves = []
        self.blackPawnMoves = []
        self.DEFAULTBlackPawnImage = ImageTk.PhotoImage(file="Pieces/images/pawn1.png")
        self.DEFAULTWhitePawnImage = ImageTk.PhotoImage(file="Pieces/images/pawn.png")
        self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        for i, j in range(1, 8):
            if self.color == "white":
                if self.board[i] == 6 and self.color == "white":
                    self.whitePawnMoves.append([i-2][j])
                else:
                    self.whitePawnMoves.append([i-1][j])
            else:
                if self.board[i] == 1 and self.color == "black":
                    self.blackPawnMoves.append([i+2][j])
                else:
                    self.blackPawnMoves.append([i+1][j])

    def initialize_image(self):
        if self.color == "black":
            self._image = self.DEFAULTBlackPawnImage
        elif self.color == "white":
            self._image = self.DEFAULTWhitePawnImage

