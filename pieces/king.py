from piece import Piece

class King(Piece):

    moved = False

    def tostring(self):
        return "K" if self.association == "White" else "k"