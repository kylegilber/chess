from pieces.piece import Piece
from board.constants import Square, Color
import numpy as np

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