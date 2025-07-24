from pieces.piece import Piece

class King(Piece):

    MOVES = [
        (1,0), (0,1), (1,1), (1,-1), 
        (-1,1),(-1,-1),(-1,0),(0,-1)
    ]

    def __init__(self):
        super().__init__()