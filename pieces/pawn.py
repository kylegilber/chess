from piece import Piece

class Pawn(Piece):

    enpassant = False

    def tostring(self):
        return 'P' if self.alliance == "White" else "p"