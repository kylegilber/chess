from pieces.piece import Piece

class Knight(Piece):

    def __init__(self): pass

    def makeAttackTable(self):
        """
        Generate attack tables for Knights.

        For each possible knight position on the board,
        update the attacks instance variable to store which
        squares the knight can attack at that position. 
        """

        for square in range(64):
            mask = self.maskAttacks(square, self.nDirections)
            self.attacks[square] = mask