from pieces.piece import Piece

class King(Piece):

    association = None
    position = None
    moved = False

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return "K" if self.association == "White" else "k"