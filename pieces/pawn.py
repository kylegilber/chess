from piece import Piece

class Pawn(Piece):

    association = None
    position = None
    enpassant = False

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'P' if self.alliance == "White" else "p"