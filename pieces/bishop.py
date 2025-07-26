from pieces.piece import Piece
import magicmoves

class Bishop(Piece):

    DIRECTIONS = [
        (1, 1), (-1, 1), (1, -1), (-1, -1)
    ]

    def __init__(self):
        self.attacks = [{} for square in range(64)]
        self.blockers = [self.maskBlockers(square, self.DIRECTIONS) for square in range(64)]

    def makeAttackTable(self):
        """
        Generate attack tables for bishops.

        For each possible bishop position on the board,
        update the attacks instance variable to store which
        squares the bishop can attack at that position.
        """

        for square in range(64):

            # Generate blockers
            mask = self.blockers[square]

            # Generate all blocker permutations
            permutations = self.permuteBlockers(mask)

            magicNum = magicmoves.bishopMagic[square]
            shiftNum = magicmoves.bishopShift[square]

            for blocker in permutations:
                index = ((blocker & mask) * magicNum) >> shiftNum
                squares = self.maskSlidingAttacks(square, self.DIRECTIONS, blocker)
                self.attacks[square][index] = squares

    def getMoves(self, square, pieces, allies):
        """
        """


