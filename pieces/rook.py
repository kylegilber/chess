from pieces.piece import Piece
import magicmoves

class Rook(Piece):

    DIRECTIONS = [
        (-1, 0), (1, 0), (0, 1), (0, -1)
    ]

    def __init__(self):
        self.attacks = [{} for square in range(64)]

    def getAttacks(self):
        """
        Generate attack tables for Rooks.

        For each possible bishop position on the board,
        update the attacks instance variable to store which
        squares the Rook can attack at that position.
        """

        for square in range(64):

            # Generate blockers
            mask = self.maskBlockers(square, self.DIRECTIONS)

            # Generate all blocker permutations
            permutations = self.permuteBlockers(mask)

            magicNum = magicmoves.rookMagic
            shiftNum = magicmoves.rookShift

            for blocker in permutations:
                index = ((blocker & mask) * magicNum) >> shiftNum
                squares = self.maskSlidingAttacks(square, self.DIRECTIONS, blocker)
                self.attacks[square][index] = squares