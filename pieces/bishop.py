from pieces.piece import Piece
import math

class Bishop(Piece):

    association = None
    position = None

    def __init__(self, assoc, pos):
        self.association = assoc
        self.position = pos

    def tostring(self):
        return 'B' if self.association == "White" else "b"
    
    def getCoords(self):
        x= self.position / 8
        y= self.position % 8
        return math.floor(x), y

    def legalMoves(self, gamestate):
        """
        :param gamestate:
        """

        moves = []
        rank, file = self.getCoords()

        if (gamestate[rank][file].piece.association == "Black"):
            x, y = rank, file
            while True:
                x += 1
                y += 1
                if (x < 8 and y < 8):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.association == "White"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x -= 1
                y += 1
                if (x > -1 and y < 8):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.assocaition == "White"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x += 1
                y -= 1
                if (x < 8 and y > -1):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.assocaition == "White"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x -= 1
                y -= 1
                if (x > -1 and y > -1):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.association == "White"):
                        moves.append([x, y])
                        break
                else: break

        else:
            x, y = rank, file
            while True:
                x += 1
                y += 1
                if (x < 8 and y < 8):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.association == "Black"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x -= 1
                y += 1
                if (x > -1 and y < 8):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.assocaition == "Black"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x += 1
                y -= 1
                if (x < 8 and y > -1):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.assocaition == "Black"):
                        moves.append([x, y])
                        break
                else: break

            x, y = rank, file
            while True:
                x -= 1
                y -= 1
                if (x > -1 and y > -1):
                    if (gamestate[x][y].piece.association is None):
                        moves.append([x, y])
                        continue
                    elif (gamestate[x][y].piece.association == "Black"):
                        moves.append([x, y])
                        break
                else: break
        return moves