from pieces.piece import Piece
import magicmoves

class Rook(Piece):

    def __init__(self):
        self.attacks = [{} for square in range(64)]
        self.blockers = [self.maskBlockers(square, self.DIRECTIONS) for square in range(64)]

    def makeAttackTable(self):
        """
        Generate attack tables for Rooks.

        For each possible Rook position on the board,
        update the attacks instance variable to store which
        squares the Rook can attack at that position.
        """

        for square in range(64):
            permutations = self.rPermutations[square]
            magic = magicmoves.rookMagic[square]
            shift = magicmoves.rookShift[square]

            for blocker in permutations:
                index = (blocker * magic) >> shift
                squares = self.maskSlidingAttacks(square, self.rDirections, blocker)
                self.attacks[square][index] = squares