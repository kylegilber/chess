from piece import Piece

class Bishop(Piece):

    association = None
    position = None

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'B' if self.association == "White" else "b"
    
    #x = Piece.getCoords()[0]
    #y = Piece.getCoords()[1]