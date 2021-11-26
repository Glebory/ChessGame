import tkinter as tk
class Mouse():
    def __init__(self, gameboard):
        self.lastx = 0
        self.lasty = 0
        self.gameboard = gameboard

    def mouseDown(self, event):
        # remember where the mouse went down
        # and where the piece was originally
        self.lastx, self.lasty = event.x, event.y


        # showLegalMoves might be better in mouseMove idk
        self.gameboard.showLegalMoves((self.lastx // self.gameboard.square_size), (self.lasty // self.gameboard.square_size))


    def mouseMove(self, event):
        # displays the chess piece as you drag it around the screen
        if self.gameboard.canvas.type(tk.CURRENT) != "rectangle":
            self.gameboard.canvas.tag_raise(tk.CURRENT)
            self.gameboard.canvas.move(tk.CURRENT, event.x - self.lastx, event.y - self.lasty)
            self.lastx = event.x
            self.lasty = event.y


    def mouseUp(self, event):
        # snaps the chess piece to a chess square
        # puts the piece in its orignal space if the move was illegal
        if self.gameboard.canvas.type(tk.CURRENT) != "rectangle":
            nearestX = ((event.x // self.gameboard.square_size) * self.gameboard.square_size)
            nearestY = ((event.y // self.gameboard.square_size) * self.gameboard.square_size)

            x = self.gameboard.canvas.coords(tk.CURRENT)[0]
            y = self.gameboard.canvas.coords(tk.CURRENT)[1]

            newX, newY = -(x - nearestX), -(y - nearestY)
            self.gameboard.canvas.move(tk.CURRENT, newX, newY)

            # update piece position
            oldX = int(self.lastx // self.gameboard.square_size)
            oldY = int(self.lasty // self.gameboard.square_size)
            targetX = int(x // self.gameboard.square_size)
            targetY = int(y // self.gameboard.square_size)

            targetSquare = False
            for piece in self.gameboard.pieces_all:
                if piece.position[0] == oldX and piece.position[1] == oldY:
                    targetPiece = piece
                else:
                    targetPiece = self.gameboard.piecesTwo[oldY][oldX]

                if piece.position[0] == targetX and piece.position[1] == targetY:
                    targetSquare = piece

            print(targetPiece)
            if self.gameboard.checkIfLegalMove(int(self.lastx // self.gameboard.square_size), int(self.lasty // self.gameboard.square_size),
                                     int(x // self.gameboard.square_size), int(y // self.gameboard.square_size), targetPiece,
                                     targetSquare) == False:
                self.gameboard.canvas.move(tk.CURRENT, -(self.gameboard.canvas.coords(tk.CURRENT)[0] - self.lastx),
                                 -(self.gameboard.canvas.coords(tk.CURRENT)[1] - self.lasty))

            else:
                for piece in self.gameboard.pieces_all:
                    if targetX == piece.position[0] and targetY == piece.position[1]:
                        self.gameboard.deletePiece(piece)
                targetPiece.position = (targetX, targetY)
                self.gameboard.piecesTwo[targetY][targetX] = self.gameboard.piecesTwo[oldY][oldX]
                self.gameboard.piecesTwo[oldY][oldX] = 0
