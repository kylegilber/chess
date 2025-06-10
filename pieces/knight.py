from piece import Piece

class Knight(Piece):

    def tostring(self):
        return 'N' if self.association == "White" else "n"