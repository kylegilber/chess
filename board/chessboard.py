import numpy as np

class Board:

    def __init__(self):
        """
        Initialize 64-bit bitboards representing chessboard
        squares for each piece type and color.
        """

        self.whiteBitBoard = np.uint64(0) 
        self.blackBitBoard = np.uint64(0) 
        self.bishopBitBoard = np.uint64(0)
        self.kingBitBoard = np.uint64(0) 
        self.knightBitBoard = np.uint64(0) 
        self.pawnBitBoard = np.uint64(0) 
        self.queenBitBoard = np.uint64(0) 
        self.rookBitBoard = np.uint64(0)