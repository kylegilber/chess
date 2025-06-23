from pieces.null import Null

class Move:

    def __init__(self): pass


    def updatePosition(self, rank, file):
        pos = rank * 8 + file
        return pos

