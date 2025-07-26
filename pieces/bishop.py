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
            magicNum = magicmoves.bishopMagic[square]
            shiftNum = magicmoves.bishopShift[square]

            for blocker in self.bPermutations:
                index = ((blocker & self.bBlockers) * magicNum) >> shiftNum
                squares = self.maskSlidingAttacks(square, self.bDirections, blocker)
                self.attacks[square][index] = squares

    def getMoves(self, square, pieces, allies):
        """
        """


