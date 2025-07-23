import numpy as np

class Board:

    def __init__(self):
        """
        Initialize 64-bit bitboards representative of 
        chessboard squares for each piece type and color.
        """

        # Pieces
        self.bishop = np.uint64(0x2400000000000024)
        self.king = np.uint64(0x1000000000000010) 
        self.knight = np.uint64(0x4200000000000042) 
        self.pawn = np.uint64(0x00FF00000000FF00) 
        self.queen = np.uint64(0x0800000000000008) 
        self.rook = np.uint64(0x8100000000000081)

        # Colors
        self.white = np.uint64(0x000000000000FFFF) 
        self.black = np.uint64(0xFFFF000000000000) 

    def getIndex(self, rank, file):
        """
        Calculate square index from coordinates.

        :arg rank: row of square
        :arg file: column of square

        :returns: index corresponding to square.
        """

        return rank * 8 + file

    def getBit(self, bitboard, index):
        """
        Get the bit state at a certain square.

        :arg bitboard: bitboard to check
        :arg index: index of square

        :returns: bit state corresponding to square.
        """

        return 1 if int(bitboard) & (1 << index) else 0