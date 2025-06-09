from pieces.Piece import Piece

class Knight(Piece):

    def tostring(self):
        return 'N' if self.association == "White" else "n"