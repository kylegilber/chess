from pieces.piece import Piece

class Rook(Piece):

    DIRECTIONS = [
        (-1, 0), (1, 0), (0, 1), (0, -1)
    ]

    def __init__(self):
        pass