from pieces.piece import Piece
from board.constants import Square, Color
import numpy as np
import math

class Pawn(Piece):

    def __init__(self):
        super().__init__()

    def getAttacks(self):
        """
        Initialize pawn attack bitboards, which are the set of 
        squares that a pawn can attack from each board position.
        """

        for square in range(64):
            bit = np.uint64(1) << square

            if (square % 8 != 0):
                self.attacks[Color.White][square] |= bit << 7
                self.attacks[Color.Black][square] |= bit >> 9
            if (square % 8 != 7):
                self.attacks[Color.White][square] |= bit << 9
                self.attacks[Color.Black][square] |= bit >> 7
    
    def tostring(self):
        return 'P' if self.association == "White" else "p"
    
    def calcCoords(self):
        rank = self.position / 8
        file = self.position % 8
        return math.floor(rank), file
    
    def legalMoves(self, gamestate):
        """
        :param gamestate: object representing chess board current state
        :returns: list containing coordinates of all legal moves
        """

        moves = []
        rank, file = self.calcCoords()

        if (self.association == "Black"):
            if (file + 1 < 8):
                if (gamestate[rank+1][file+1].piece.association == "White"):
                    moves.append([rank+1, file+1])
            if (file - 1 > -1):
                if (gamestate[rank+1][file-1].piece.association == "White"):
                    moves.append([rank+1][file-1])
            if (rank == 1):
                if (gamestate[rank+1][file].piece.association is None):
                    moves.append([rank+1, file])
                if (gamestate[rank+2][file].piece.association is None):
                    moves.append([rank+2, file])
            else:
                if (gamestate[rank+1][file].piece.association is None):
                    moves.append([rank+1, file])
        else:
            if (file + 1 < 8):
                if (gamestate[rank-1][file+1].piece.association == "Black"):
                    moves.append([rank-1, file+1])
            if (file - 1 > -1):
                if (gamestate[rank-1][file-1].piece.association == "Black"):
                    moves.append([rank-1][file-1])
            if (rank == 6):
                if (gamestate[rank-1][file].piece.association is None):
                    moves.append([rank-1, file])
                if (gamestate[rank-2][file].piece.association is None):
                    moves.append([rank-2, file])
            else:
                if (gamestate[rank-1][file].piece.association is None):
                    moves.append([rank-1, file])

        return moves