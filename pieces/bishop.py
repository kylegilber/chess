from pieces.Piece import Piece

class Bishop(Piece):

    def __init__(self, assoc = None, pos = None):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'B' if self.association == "White" else "b"