from pieces.piece import Piece
from board.constants import Color
import numpy as np

class Pawn(Piece):

    def __init__(self):
        self.attacks = [[0 for square in range(64)] for color in range(2)]

    def makeAttackTable(self):
        """
        Initialize attack bitboards for pawns. 
        
        For each possible pawn position on the board,
        update the attacks instance variable to store which
        squares pawns of each color can attack at that position. 
        """

        for square in range(64):
            bit = np.uint64(1) << square

            if (square % 8 != 0):
                self.attacks[Color.White][square] |= bit << 7
                self.attacks[Color.Black][square] |= bit >> 9
            if (square % 8 != 7):
                self.attacks[Color.White][square] |= bit << 9
                self.attacks[Color.Black][square] |= bit >> 7