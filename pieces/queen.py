from pieces.piece import Piece
import math

class Queen(Piece):

    association = None
    position = None
    directions = [(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1)]

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'Q' if self.association == "White" else "q"
    
    def calcCoords(self):
        rank = self.position / 8
        file = self.position % 8
        return math.floor(rank), file
    
    def legalMoves(self, gamestate):
        """
        """

        moves = []
        rank, file = self.calcCoords()

        for dir in self.directions:
            tempr, tempf = rank, file

            while True:
                tempr += dir[0]
                tempf += dir[1]
                if (-1 < tempr < 8 and -1 < tempf < 8):
                    assoc = gamestate[tempr][tempf].piece.association
                    if (assoc is None): 
                        moves.append([tempr, tempf])
                        continue
                    elif (assoc != self.association):
                        moves.append([tempr, tempf])
                        break
                    else: break
                else: break
                
        return moves

        