from pieces.piece import Piece

class Queen(Piece):

    directions = [(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1)]

    def __init__(self): pass