from pieces.piece import Piece

class Knight(Piece):

    MOVES = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    def __init__(self):
        super().__init__()

    def makeAttackTable(self):
        """
        Generate attack tables for Knights.

        For each possible knight position on the board,
        update the attacks instance variable to store which
        squares the knight can attack at that position. 
        """

        for square in range(64):
            mask = self.maskAttacks(square, self.MOVES)
            self.attacks[square] = mask