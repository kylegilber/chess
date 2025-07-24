from pieces.piece import Piece

class Bishop(Piece):

    MOVES = [
        (1, 1), (-1, 1), (1, -1), (-1, -1)
    ]

    def __init__(self):
        super().__init__()

    