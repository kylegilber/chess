from pieces.piece import Piece

class Knight(Piece):

    association = None
    position = None

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'N' if self.association == "White" else "n"