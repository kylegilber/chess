from pieces.piece import Piece
import math

class Bishop(Piece):

    association = None
    position = None
    directions = [(1,1),(-1,1),(1,-1)(-1,-1)]

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'B' if self.association == "White" else "b"
    
    def calcCoords(self):
        rank = self.position / 8
        file = self.position % 8
        return math.floor(rank), file

    def legalMoves(self, gamestate):
        """
        :param gamestate: board object representing the current state of the chess game
        :returns: a list containing the coordinates of all legal moves for a Bishop object
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
                    if (assoc != self.association):
                        moves.append([tempr, tempf])
                        break
                else: break
                
        return moves