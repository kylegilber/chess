from pieces.piece import Piece
import magicmoves

class Queen(Piece):

    def __init__(self):
        self.attacks = [{} for square in range(64)]

    def makeAttackTable(self):
        """
        Generate attack tables for Queens.

        For each possible Queen position on the board,
        update the attacks instance variable to store which
        squares the Queen can attack at that position.
        """

        for square in range(64):

            bMask = self.bBlockers[square]
            rMask = self.rBlockers[square]

            bPermutations = self.bPermutations[square]
            rPermutations = self.rPermutations[square]

            bMagic = magicmoves.bishopMagic[square]
            bShift = magicmoves.bishopShift[square]
            rMagic = magicmoves.rookMagic[square]
            rShift = magicmoves.rookShift[square]

            for blocker in bPermutations:
                index = ((blocker & bMask) * bMagic) >> bShift
                squares = self.maskSlidingAttacks(square, self.bDirections, blocker)
                self.attacks[square][index] = squares

            for blocker in rPermutations:
                index = ((blocker & rMask) * rMagic) >> rShift
                squares = self.maskSlidingAttacks(square, self.rDirections, blocker)
                
                if (index in self.attacks[square]):
                    self.attacks[square][index] |= squares
                else: self.attacks[square][index] = squares




