from piece import Piece

class Queen(Piece):

    def tostring(self):
        return 'Q' if self.association == "White" else "q"