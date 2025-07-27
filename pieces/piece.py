import numpy as np
import magicmoves

class Piece:

    bDirections = [(1,1),(-1,1),(1,-1),(-1,-1)]
    kDirections = [(1,0),(0,1),(1,-1),(-1,-1),(-1,1),(1,1),(-1,0),(0,-1)]
    nDirections = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    rDirections = [(-1,0),(1,0),(0,1),(0,-1)]

    def __init__(self):

        # Init attack table for non-sliding pieces
        self.attacks = [0 for square in range(64)]

        # Get diagonal blockers
        self.bBlockers = [
            self.maskBlockers(square, self.bDirections) for square in range(64)
        ]

        # Get orthogonal blockers
        self.rBlockers = [
            self.maskBlockers(square, self.rDirections) for square in range(64)
        ]

        # Permute diagonal blockers
        self.bPermutations = self.permuteBlockers(self.bBlockers)

        # Permute orthogonal blockers
        self.rPermutations = self.permuteBlockers(self.rBlockers)

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

    def maskAttacks(self, square, directions):
        """
        Generate attack bitboards for color-independent 
        pieces from a list of their possible movements.

        {args}
        square (int): index of square
        directions (list): rank, file tuples

        {returns}
        Bitboard with attack squares set to 1.
        """

        # Init empty bitboard
        mask = np.uint64(0)
        rank, file = self.getCoord(square)

        for xrank, xfile in directions:
            r = rank + xrank
            f = file + xfile

            # Accumulate valid attacks
            if (-1 < r < 8 and -1 < f < 8):
                index = self.getIndex(r, f)
                mask |= np.uint64(1) << index

        return mask
    
    def maskBlockers(self, square, directions):
        """
        Generate bitboards of positions blocking the movement of sliding pieces.

        {args}
        square (int): index of square
        directions (list): rank, file tuples

        {returns}
        mask (uint64): bitboard with blocking squares set to 1.
        """
        
        mask = np.uint64(0)
        rank, file = self.getCoord(square)

        for xrank, xfile in directions:
            r = rank + xrank
            f = file + xfile

            while (0 < r < 7) and (0 < f < 7):
                index = self.getIndex(r, f)
                mask |= np.uint64(1) << index
                r += xrank
                f += xfile

        return mask
    
    def permuteBlockers(self, mask):
        """
        Generate all blocker permutations for a given bitboard.

        {args}
        mask (uint64): bitboard representing all blockers

        {returns}
        list[int]: unique permutations of blockers
        """

        permutations = []

        # Get indices of "set" bits
        bits = [square for square in range(64) if ((mask >> square) &  1)]

        # Bitmask enumeration
        for permutation in range(1 << len(bits)):
            blockers = 0
            for pos, index in enumerate(bits):
                if ((permutation >> pos) & 1):
                    blockers |= 1 << index
            permutations.append(blockers)

        return permutations
    
    def maskSlidingAttacks(self, square, directions, blockers):
        """
        Generate bitboard of attacks for a sliding piece.

        {args}
        square (int): index of given square
        directions (list): rank, file tuples 
        blockers (uint64): bitboard of blocked squares

        {returns}
        mask (uint64): bitboard with legal attack squares set to 1.
        """

        # Init empty bitboard
        mask = np.uint64(0)
        rank, file = self.getCoord(square)

        for xrank, xfile in directions:
            r = rank + xrank
            f = file + xfile

            # Accumulate valid attacks
            while (-1 < r < 8) and (-1 < f < 8):
                index = self.getIndex(r, f)
                mask |= np.uint64(1) << index

                if (blockers & (np.uint64(1) << index)):
                    break

                r += xrank
                f += xfile

        return mask
    
    def getMagicShift(self, piece, square):
        """
        Helper function for accessing magic & shift numbers for a given square.

        {args}
        piece (str): bishop 'b' or rook 'r'
        square (int): index of square

        {returns}
        Magic & shift nums corresponding to piece, square.
        """

        if (piece == 'b'): 
            return magicmoves.bishopMagic[square], magicmoves.bishopShift[square]
        elif (piece == 'r'):
            return magicmoves.rookMagic[square], magicmoves.rookShift[square]
        else: 
            raise ValueError(f"Unrecognized piece: {piece}.")

