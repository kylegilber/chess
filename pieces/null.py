from pieces.piece import Piece

class Null(Piece):
    
    def __init__(self):
        self.association = None

    def tostring(self):
        return "-"