import tkinter as tk
from tkinter import ttk
from Pieces.Bishop import *
from Pieces.King import *
from Pieces.Knight import *
from Pieces.Pawn import *
from Pieces.Queen import *
from Pieces.Rook import *
#import game

square_size = 64
rows = 8
cols = 8
WHITE_COLOUR = "#ffffff"
DARKGREEN_COLOUR = "#006600"

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")

class mainMenu(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        playGameButton = tk.Button(self, text="Play Game", command=self.playgamebuttonpressed)
        watchGameButton = tk.Button(self, text="Watch Game", command="watchgamebuttonpressed")
        settingsButton = tk.Button(self, text="Settings", command="settingsbuttonpressed")
        exitButton = tk.Button(self, text="Exit", command=tk._exit)

        self.place(relx=.5, rely=.5, anchor="center")
        playGameButton.grid(row=0, ipadx=64, sticky ="N, E, S, W")
        watchGameButton.grid(row=1, ipadx=64, sticky ="N, E, S, W")
        settingsButton.grid(row=2, ipadx=64, sticky ="N, E, S, W")
        exitButton.grid(row=3, ipadx=64, sticky ="N, E, S, W")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

    def playgamebuttonpressed(self):
        self.destroy()
        board = GameBoard(app)
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        board.mainloop()

class GameBoard(ttk.Frame):
    def __init__(self, parent):
        #self.window = Tk()
        #self.window.title("Chess Game")
        tk.Frame.__init__(self, parent)
        self.square_size = 64
        self.canvas = tk.Canvas(self, width=square_size * cols, height=square_size * rows)
        self.canvas.pack()
        self.play_again()

        tk.Widget.bind(self.canvas, "<1>", self.mouseDown)
        tk.Widget.bind(self.canvas, "<B1-Motion>", self.mouseMove)
        tk.Widget.bind(self.canvas, "<ButtonRelease-1>", self.mouseUp)
    

    def mouseDown(self, event):
        #remember where the mouse went down
        #and where the piece was originally
        self.lastx = event.x
        self.lasty = event.y
        self.originalX = self.canvas.coords(tk.CURRENT)[0]
        self.originalY = self.canvas.coords(tk.CURRENT)[1]
        #showLegalMoves might be better in mouseMove idk
        self.showLegalMoves((self.originalX//self.square_size), (self.originalY//self.square_size))
        

    def mouseMove(self, event):
        #displays the chess piece as you drag it around the screen
        if self.canvas.type(tk.CURRENT) != "rectangle":
            self.canvas.tag_raise(tk.CURRENT)
            self.canvas.move(tk.CURRENT, event.x - self.lastx, event.y - self.lasty)
            self.lastx = event.x
            self.lasty = event.y

    def mouseUp(self, event):
        #snaps the chess piece to a chess square
        #puts the piece in its orignal space if the move was illegal
        if self.canvas.type(tk.CURRENT) != "rectangle":
            nearestX = ((event.x // self.square_size) * square_size)
            nearestY = ((event.y // self.square_size) * square_size)

            x = self.canvas.coords(tk.CURRENT)[0]
            y = self.canvas.coords(tk.CURRENT)[1]

            newX, newY = -(x-nearestX), -(y-nearestY)
            self.canvas.move(tk.CURRENT, newX, newY)

            #update piece position
            oldX = int(self.originalX//self.square_size)
            oldY = int(self.originalY//self.square_size)
            targetX = int(x//self.square_size)
            targetY = int(y//self.square_size)

            targetSquare = False
            for piece in self.pieces_all:
                    if piece.position[0] ==  oldX and piece.position[1] == oldY:
                        targetPiece = piece
                    else:
                        targetPiece = self.piecesTwo[oldY][oldX]

                    if piece.position[0] == targetX and piece.position[1] == targetY:
                        targetSquare = piece

            print(targetPiece)
            if self.checkIfLegalMove(int(self.originalX//self.square_size), int(self.originalY//self.square_size), int(x//self.square_size), int(y//self.square_size), targetPiece, targetSquare) == False:
                self.canvas.move(tk.CURRENT, -(self.canvas.coords(tk.CURRENT)[0]-self.originalX), -(self.canvas.coords(tk.CURRENT)[1]-self.originalY))

            else:
                for piece in self.pieces_all:
                    if targetX == piece.position[0] and targetY == piece.position[1]:
                        self.deletePiece(piece)
                targetPiece.position = (targetX, targetY)
                self.piecesTwo[targetY][targetX] = self.piecesTwo[oldY][oldX]
                self.piecesTwo[oldY][oldX] = 0                

    def deletePiece(self, dyingPiece):
        print("##deleting##")
        #delete from piece matrix and the lists
        #x, y = dyingPiece.position[0], dyingPiece.position[1]
        #self.canvas.delete(self.pieces[0][1])
        #self.pieces[y].pop(x)
        #self.piecesTwo[y].pop(x)
        
        #self.pieces_all.remove(dyingPiece)
        

    def checkBlocked(self, currentPiece, endx, endy):
        tempStartx = currentPiece.position[0]
        tempStartY = currentPiece.position[1]

        while tempStartx != endx or tempStartY != endy:
            if endx != tempStartx:
                if endx > tempStartx:
                    tempStartx += 1
                elif endx < tempStartx:
                    tempStartx -= 1
            if endy != tempStartY:
                if endy > tempStartY:
                    tempStartY += 1
                elif endy < tempStartY:
                    tempStartY -= 1
                    
            for piece in self.pieces_all:
                if piece.position[0] ==  tempStartx and piece.position[1] == tempStartY:
                    if piece.position[0] == endx and piece.position[1] == endy:
                        pass
                        #if the piece blocking is on the last square then its trying to take instead
                        #colour doesnt matter it was filtered out in legal moves first
                        return True
                    if type(currentPiece).__name__ != "Knight":
                        #if theres a piece in the path
                        #i want to know is it the last piece
                        print("blocked")
                        return False


    def checkIfLegalMove(self, startCoordX, startCoordY, endCoordX, endCoordY, currentPiece, targetSquare):
        availableMoves = currentPiece.check_valid_moves()
        valid = False
        if targetSquare != False:
            if currentPiece.color == targetSquare.color:
                return False
        for i in availableMoves:
            if i[0] == endCoordX and i[1] == endCoordY:
                valid = True
        if valid == False or self.checkBlocked(currentPiece, endCoordX, endCoordY) == False:
            return False            

    def showLegalMoves(self, x, y):
        pass

    def initialize_board(self):
        #creates a chess board and places the pieces
        #and stores the squares in a board matrix
        squareMatrix = [0] * rows
        for x in range(cols):
            squareMatrix[x] = [0] * cols

        self.board = squareMatrix

        self.pieces = squareMatrix

        self.piecesTwo = squareMatrix

        self.pieces_all = []

        self.row0 = [Rook("white", self,(0,0)),
        Knight("white", self,(1, 0)),
        Bishop("white", self,(2, 0)),
        King("white", self,(3, 0)),
        Queen("white", self,(4, 0)),
        Bishop("white", self,(5, 0)),
        Knight("white", self, (6, 0)),
        Rook("white", self,(7, 0))]

        self.row1 = [Pawn("white", self, (0, 1)),
        Pawn("white", self, (1, 1)),
        Pawn("white", self, (2, 1)),
        Pawn("white", self, (3, 1)),
        Pawn("white", self, (4, 1)),
        Pawn("white", self, (5, 1)),
        Pawn("white", self, (6, 1)),
        Pawn("white", self, (7, 1))]

        self.row6 = [Pawn("black", self, (0, 6)),
        Pawn("black", self, (1, 6)),
        Pawn("black", self, (2, 6)),
        Pawn("black", self, (3, 6)),
        Pawn("black", self, (4, 6)),
        Pawn("black", self, (5, 6)),
        Pawn("black", self, (6, 6)),
        Pawn("black", self, (7, 6))]

        self.row7 = [Rook("black", self, (0, 7)),
        Knight("black", self, (1, 7)),
        Bishop("black", self, (2, 7)),
        King("black", self, (3, 7)),
        Queen("black", self, (4, 7)),
        Bishop("black", self, (5, 7)),
        Knight("black", self, (6, 7)),
        Rook("black", self, (7, 7))]

        self.pieces_all += self.row0 + self.row1 + self.row6 + self.row7

        colour = DARKGREEN_COLOUR

        for row in range(rows):
            colour = self.changeColour(colour)
            for col in range(cols):
                x1 = (col * self.square_size)
                y1 = (row * self.square_size)
                x2 = (x1 + self.square_size)
                y2 = (y1 + self.square_size)
                self.board[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=colour, tags="square")

                #temporary items for testing, will update for later versions
                #www.opengameart.org/content/pixel-chess-pieces
                #Author - Lucas312
                #CC BY 3.0
                #CC BY-SA 3.0

                # create canvas returns an integer id number for that object
                # tagOrId argument can be used to reference this
                colour = self.changeColour(colour)

        for a in range(cols):
            self.pieces[0][a] = self.canvas.create_image(a*self.square_size, 0, image = self.row0[a].image, anchor='nw')
            self.piecesTwo[0][a] = self.row0[a]

        for b in range(cols):
            self.pieces[1][b] = self.canvas.create_image(b*self.square_size, 64, image = self.row1[b].image, anchor='nw')
            self.piecesTwo[1][b] = self.row1[b]

        for c in range(cols):
            self.pieces[6][c] = self.canvas.create_image(c*self.square_size, 384, image = self.row6[c].image, anchor='nw')
            self.piecesTwo[6][c] = self.row6[c]

        for d in range(cols):
            self.pieces[7][d] = self.canvas.create_image(d*self.square_size, 448, image = self.row7[d].image, anchor='nw')
            self.piecesTwo[7][d] = self.row7[d]

    def changeColour(self, colour):
        if colour == DARKGREEN_COLOUR:
            colour = WHITE_COLOUR
        else:
            colour = DARKGREEN_COLOUR
        return colour

    def play_again(self):
        self.canvas.delete("all")
        self.initialize_board()

if __name__ == "__main__":
    app = GUI()
    frame = mainMenu(app)
    app.mainloop()