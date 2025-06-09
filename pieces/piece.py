import math

class Piece:

    def __init__(self, assoc = None, pos = None):
        self.association = assoc
        self.position = pos

    def getCoords(self):
        a=self.position/8
        b=self.position%8
        return[math.floor(a),b]