class Piece:

    WHITE = 0
    BLACK = 1

    def __init__(self):
        self.moves = [[0 for square in range(64)] for color in range(2)]

    