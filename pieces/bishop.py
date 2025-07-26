from pieces.piece import Piece
import magicmoves

class Bishop(Piece):

    def __init__(self):
        self.attacks = [{} for square in range(64)]

    def makeAttackTable(self):
        """
        Generate attack tables for bishops.

        For each possible bishop position on the board,
        update the attacks instance variable to store which
        squares the bishop can attack at that position.
        """

        for square in range(64):

            permutations = self.bPermutations[square]
            magic = magicmoves.bishopMagic[square]
            shift = magicmoves.bishopShift[square]

            for blocker in permutations:
                index = (blocker * magic) >> shift
                squares = self.maskSlidingAttacks(square, self.bDirections, blocker)
                self.attacks[square][index] = squares

    def getAttacks(self, square, blockers):
        """
        Get pseudo-legal Bishop attacks.

        {args}
        square (int): index of square
        blockers (uint64): bitboard of blockers

        {returns}
        Bitboard (uint64) of attackable squares.
        """

        magic = magicmoves.bishopMagic[square]
        shift = magicmoves.bishopShift[square]
        index = (blockers * magic) >> shift

        return self.attacks[square][index]
     
    def getMoves(self, square, pieces, allies):
        """
        """


