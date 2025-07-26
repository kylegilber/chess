from pieces.piece import Piece

class King(Piece):

    def __init__(self): pass

    def makeAttackTable(self):
        """
        Generate attack tables for Kings.

        For each possible knight position on the board, update 
        self.attacks to store which squares the king can attack
        at that position.
        """

        for square in range(64):
            mask = self.maskAttacks(square, self.kDirections)
            self.attacks[square] = mask