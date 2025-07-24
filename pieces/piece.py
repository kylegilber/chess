class Piece:

    def __init__(self):
        self.attacks = [[0 for square in range(64)] for color in range(2)]

    