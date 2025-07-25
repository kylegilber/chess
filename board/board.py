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

    def getBit(self, bitboard, index):
        """
        Get the bit state at an index.

        {args}
        bitboard (uint64): bitboard to check
        index (int): index of square

        {returns} 
        Bit state at index corresponding to a square.
        """

        return 1 if int(bitboard) & (1 << index) else 0
    
    def setBit(self, bitboard, index):
        """
        Set the bit state to 1 at an index.

        :args:
        bitboard (uint64) - bitboard to check
        index (int) - index of square

        :returns: New bitboard with bit at index set to 1.
        """

        return int(bitboard) | (1 << index)
    
    def popBit(self, bitboard, index):
        """
        Clear the bit at an index.

        :args:
        bitboard (uint64) - bitboard to check
        index (int) - index of square

        :returns: New bitboard with bit at index set to 0.
        """

        return int(bitboard) & ~(1 << index)