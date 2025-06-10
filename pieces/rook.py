from piece import Piece

class Rook(Piece):

    association = None
    position = None
    moved = False

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'R' if self.association == 'White' else 'r'