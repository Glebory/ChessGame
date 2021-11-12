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

            if self.checkIfLegalMove(int(self.originalX//self.square_size), int(self.originalY//self.square_size), int(x//self.square_size), int(y//self.square_size)) == False:
                self.canvas.move(tk.CURRENT, -(self.canvas.coords(tk.CURRENT)[0]-self.originalX), -(self.canvas.coords(tk.CURRENT)[1]-self.originalY))

    def checkIfLegalMove(self, startCoordX, startCoordY, endCoordX, endCoordY):
        pass

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

        self.row0 = [Rook("white", self,(0,0)),
        Knight("white", self,(0,1)),
        Bishop("white", self,(0,2)),
        King("white", self,(0,3)),
        Queen("white", self,(0,4)),
        Bishop("white", self,(0,5)),
        Knight("white", self, (0, 6)),
        Rook("white", self,(0,7))]

        self.row1 = [Pawn("white", self, (1, 0)),
        Pawn("white", self, (1, 1)),
        Pawn("white", self, (1, 2)),
        Pawn("white", self, (1, 3)),
        Pawn("white", self, (1, 4)),
        Pawn("white", self, (1, 5)),
        Pawn("white", self, (1, 6)),
        Pawn("white", self, (1, 7))]

        self.row6 = [Pawn("black", self, (6, 0)),
        Pawn("black", self, (6, 1)),
        Pawn("black", self, (6, 2)),
        Pawn("black", self, (6, 3)),
        Pawn("black", self, (6, 4)),
        Pawn("black", self, (6, 5)),
        Pawn("black", self, (6, 6)),
        Pawn("black", self, (6, 7))]

        self.row7 = [Rook("black", self, (7, 0)),
        Knight("black", self, (7, 1)),
        Bishop("black", self, (7, 2)),
        King("black", self, (7, 3)),
        Queen("black", self, (7, 4)),
        Bishop("black", self, (7, 5)),
        Knight("black", self, (7, 6)),
        Rook("black", self, (7, 7))]


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

        for b in range(cols):
            self.pieces[1][b] = self.canvas.create_image(b*self.square_size, 64, image = self.row1[b].image, anchor='nw')

        for c in range(cols):
            self.pieces[6][c] = self.canvas.create_image(c*self.square_size, 384, image = self.row6[c].image, anchor='nw')

        for d in range(cols):
            self.pieces[7][d] = self.canvas.create_image(d*self.square_size, 448, image = self.row7[d].image, anchor='nw')

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