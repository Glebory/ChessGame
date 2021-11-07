import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
#import objects
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
        self.showLegalMoves((self.originalX//square_size), (self.originalY//square_size))

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
            nearestX = ((event.x // square_size) * square_size)
            nearestY = ((event.y // square_size) * square_size)

            x = self.canvas.coords(tk.CURRENT)[0]
            y = self.canvas.coords(tk.CURRENT)[1]

            newX, newY = -(x-nearestX), -(y-nearestY)
            self.canvas.move(tk.CURRENT, newX, newY)

            if self.checkIfLegalMove(int(self.originalX//square_size), int(self.originalY//square_size), int(x//square_size), int(y//square_size)) == False:
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

        self.blackPawnImage = ImageTk.PhotoImage(file="images/pawn1.png")
        self.blackBishopImage = ImageTk.PhotoImage(file="images/bishop1.png")
        self.blackKingImage = ImageTk.PhotoImage(file="images/king1.png")
        self.blackKnightImage = ImageTk.PhotoImage(file="images/knight1.png")
        self.blackQueenImage = ImageTk.PhotoImage(file="images/queen1.png")
        self.blackRookImage = ImageTk.PhotoImage(file="images/rook1.png")

        self.whitePawnImage = ImageTk.PhotoImage(file="images/pawn.png")
        self.whiteBishopImage = ImageTk.PhotoImage(file="images/bishop.png")
        self.whiteKingImage = ImageTk.PhotoImage(file="images/king.png")
        self.whiteKnightImage = ImageTk.PhotoImage(file="images/knight.png")
        self.whiteQueenImage = ImageTk.PhotoImage(file="images/queen.png")
        self.whiteRookImage = ImageTk.PhotoImage(file="images/rook.png")

        row0=[self.blackRookImage,
              self.blackKnightImage,
              self.blackBishopImage,
              self.blackKingImage,
              self.blackQueenImage,
              self.blackBishopImage,
              self.blackKnightImage,
              self.blackRookImage]

        row7=[self.whiteRookImage,
              self.whiteKnightImage,
              self.whiteBishopImage,
              self.whiteKingImage,
              self.whiteQueenImage,
              self.whiteBishopImage,
              self.whiteKnightImage,
              self.whiteRookImage]

        colour = DARKGREEN_COLOUR

        for row in range(rows):
            colour = self.changeColour(colour)
            for col in range(cols):
                x1 = (col * square_size)
                y1 = (row * square_size)
                x2 = (x1 + square_size)
                y2 = (y1 + square_size)
                self.board[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=colour, tags="square")

                #temporary items for testing, will update for later versions
                #www.opengameart.org/content/pixel-chess-pieces
                #Author - Lucas312
                #CC BY 3.0
                #CC BY-SA 3.0

                # create canvas returns an integer id number for that object
                # tagOrId argument can be used to reference this
                if row == 1:
                    self.pieces[row][col] = self.canvas.create_image(x1, y1, image=self.blackPawnImage, anchor='nw')
                elif row == 6:
                    self.pieces[row][col] = self.canvas.create_image(x1, y1, image=self.whitePawnImage, anchor='nw')
                colour = self.changeColour(colour)

        for a in range(cols):
            self.pieces[0][a] = self.canvas.create_image(a*square_size, 0, image = row0[a], anchor='nw')

        for b in range(cols):
            self.pieces[7][b] = self.canvas.create_image(b*square_size, 448, image = row7[b], anchor='nw')

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