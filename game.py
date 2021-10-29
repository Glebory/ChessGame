from tkinter import *
from objects import *

class Game:
    def __init__(self):
        self._game_matrix = self.setGame()
        self._game_objects = []
    def setGame(self):
        matrix = [[0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0]]
        for val in range(matrix):
            w_pawn = objects.Pawn("w",val+1)
            b_pawn = objects.Pawn("b", val+1)
            matrix[1] += w_pawn
            matrix[6] += b_pawn
            self._game_objects += w_pawn, b_pawn
        list1 =[objects.Rook("b",0),
        objects.Knight("b",1),
        objects.Bishop("b",2),
        objects.King("b",3),
        objects.Queen("b",4),
        objects.Rook("w",0),
        objects.Knight("w",1),
        objects.Bishop("w",2),
        objects.King("w",3),
        objects.Queen("w",4),
        objects.Rook("b",7),
        objects.Knight("b",6),
        objects.Bishop("b",5),
        objects.Rook("w",7),
        objects.Knight("w",6),
        objects.Bishop("w",5)]
        for val in list1:
            matrix[val.y][val.x] += val


    def startGame(self):

    def stopGame(self):

    def runGame(self):

def main():



