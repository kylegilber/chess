from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.null import Null
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from board.square import Square
import numpy as np

class Board:

    def __init__(self):
        self.white = np.uint64(0) 
        self.black = np.uint64(0) 
        self.bishop = np.uint64(0)
        self.king = np.uint64(0) 
        self.knight = np.uint64(0) 
        self.pawn = np.uint64(0) 
        self.queen = np.uint64(0) 
        self.rook = np.uint64(0)

    gamestate = [[0 for rank in range(8)] for file in range(8)]

    def setupBoard(self):
        """
        Set up the initial chess board state
        """

        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for file in range(8):
            self.gamestate[0][file] = Square(file, order[file]("Black", file))
            self.gamestate[1][file] = Square(file + 8, Pawn("Black", file + 8))
            self.gamestate[6][file] = Square(file + 48, Pawn("White", file + 48))
            self.gamestate[7][file] = Square(file + 56, order[file]("White", file + 56))

        for rank in range(2, 6):
            for file in range(8):
                self.gamestate[rank][file] = Square(rank * 8 + file, Null())

    def printBoard(self):
        """
        Print the current board state
        """

        for rank in range(8):
            for file in range(8):
                print("|", self.gamestate[rank][file].piece.tostring(), end= "")
            print("|")