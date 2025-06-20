from pieces.piece import Piece
import math

class King(Piece):

    association = None
    position = None
    moved = False
    directions = [(1,0),(0,1),(1,1),(1,-1),(-1,1),(-1,-1),(-1,0),(0,-1)]

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return "K" if self.association == "White" else "k"
    
    def calcCoords(self):
        rank = self.position / 8
        file = self.position % 8
        return math.floor(rank), file
    
    def legalMoves(self, gamestate):
        """
        :param gamestate: object representing chess board current state
        :returns: list containing coordinates of all legal moves
        """

        moves = []
        rank, file = self.calcCoords()

        for dir in self.directions:
            tempr, tempf = rank + dir[0], file + dir[1]
            if (-1 < tempr < 8 and -1 < tempf < 8):
                if (gamestate[tempr][tempf].piece.association != self.association):
                    moves.append([tempr, tempf])
        
        return moves