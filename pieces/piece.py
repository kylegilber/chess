import math

class Piece:

    def __init__(self): pass

    def getCoords(self):
        a=self.position/8
        b=self.position%8
        return[math.floor(a),b]