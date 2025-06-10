from piece import Piece

class Rook(Piece):

    moved = False

    def tostring(self):
        return 'R' if self.association == 'White' else 'r'