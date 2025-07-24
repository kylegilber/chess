from pieces.piece import Piece

class King(Piece):

    MOVES = [
        (1, 0), (0, 1), (1, -1), (-1, -1),
        (-1, 1), (1, 1), (-1, 0), (0, -1)
    ]

    def __init__(self):
        super().__init__()

    def getAttacks(self):
        """
        Generate attack tables for Kings.

        For each possible knight position on the board, update 
        self.attacks to store which squares the king can attack
        at that position.
        """

        for square in range(64):
            mask = self.maskAttacks(square, self.MOVES)
            self.attacks[square] = mask