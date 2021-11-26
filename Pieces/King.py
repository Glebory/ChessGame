from PIL import ImageTk
from Chessticles.Pieces import GameObjects


class King(GameObjects.GameObjects):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
      #  self.DEFAULTBlackKingImage = ImageTk.PhotoImage(file="Pieces/images/king1.png")
       # self.DEFAULTWhiteKingImage = ImageTk.PhotoImage(file="Pieces/images/king.png")
        #self.initialize_image()

    def __str__(self):
        return "%s %s" % (self.color, self.position)

    def check_valid_moves(self):
        king_moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= self.position[0] + x <= 7 and self.position[1] + y >= 0 and self.position[1] + x <= 7:
                    king_moves += [(self.position[0] + x, self.position[1] + y)]
        return king_moves

 #   def initialize_image(self):
  #      if self.color == "black":
   #         self.image = self.DEFAULTBlackKingImage
    #    elif self.color == "white":
     #       self.image = self.DEFAULTWhiteKingImage
      #  return self.image
