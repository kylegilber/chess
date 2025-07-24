import numpy as np

class Piece:

    def __init__(self):
        self.attacks = [0 for square in range(64)]

    def getCoord(self, index):
        """
        Convert square index to coordinates.

        {args}
        index (int): index corresp to square

        {returns}
        The square's rank & file coordinates.
        """

        rank = index // 8
        file = index % 8
        return rank, file
    
    def getIndex(self, rank, file):
        """
        Calculate square index from coordinates.

        {args}
        rank (int): row of square
        file (int): column of square

        {returns} index corresponding to square.
        """

        return rank * 8 + file

    def maskAttacks(self, square, moves):
        """
        Generate attack bitboards for color-independent 
        pieces from a list of their possible movements.

        {args}
        square (int): index of square
        moves (list): rank, file tuples

        {returns}
        Bitboard with attack squares set to 1
        """

        # Init empty bitboard
        mask = np.uint64(0)

        rank, file = self.getCoord(square)
        for xrank, xfile in moves:
            r = rank + xrank
            f = file + xfile

            # Accumulate valid attacks
            if (-1 < r < 8 and -1 < f < 8):
                index = self.getIndex(r, f)
                mask |= np.uint64(1) << index

        return mask



