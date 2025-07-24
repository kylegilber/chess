from pieces.piece import Piece
import numpy as np

class Knight(Piece):

    MOVES = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    def __init__(self):
        super().__init__()

    def getAttacks(self):
        """
        Initialize attack bitboards for knights.

        For each possible knight position on the board,
        update the attacks instance variable to store which
        squares the knight can attack at that position. 
        """

        for square in range(64):

            # Create bitboard with knight on square
            bit = np.uint64(1) << square

            # Init empty bitboard
            mask = np.uint64(0)

            rank, file = self.getCoord(square)

            # Check if each move is inbounds
            for xr, xf in self.MOVES:
                r, f = xr + rank, xf + file
                if (-1 < r < 8 and -1 < f < 8):
                    index = self.getIndex(r, f)
                    mask |= np.uint64(1) << index
            
            # Accumulate knight's legal attacks
            self.attacks[square] = mask