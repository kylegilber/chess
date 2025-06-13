from pieces.piece import Piece

class Queen(Piece):

    association = None
    position = None

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'Q' if self.association == "White" else "q"