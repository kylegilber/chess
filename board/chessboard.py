import numpy as np

class Board:

    def __init__(self):
        """
        Initialize 64-bit bitboards representing chessboard
        squares for each piece type and color.
        """

        self.white = np.uint64(0) 
        self.black = np.uint64(0) 
        self.bishop = np.uint64(0)
        self.king = np.uint64(0) 
        self.knight = np.uint64(0) 
        self.pawn = np.uint64(0) 
        self.queen = np.uint64(0) 
        self.rook = np.uint64(0)