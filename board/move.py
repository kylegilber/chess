from pieces.null import Null

class Move:

    def __init__(self): pass


    def updatePosition(self, rank, file):
        pos = rank * 8 + file
        return pos

    def enpassant(self, gamestate, rank, file):
        """
        """

        moves = []
        cur = gamestate[rank][file].piece

        if (rank == 4):
            if (cur.tostring() == "p"):
                if (file + 1 < 8):
                    temp = gamestate[rank][file+1].piece
                    if (temp.tostring() == "P" and temp.enpassant == True):
                        moves.append([rank, file+1])
                if (file - 1 > -1):
                    temp = gamestate[rank][file-1].piece
                    if (temp.tostring() == "P" and temp.enpassant == True):
                        moves.append([rank, file-1])
        elif (rank == 3):
            if (cur.tostring() == "P"):
                if (file + 1 < 8):
                    temp = gamestate[rank][file+1].piece
                    if (temp.tostring() == "p" and temp.enpassant == True):
                        moves.append([rank, file+1])
                if (file - 1 > -1):
                    temp = gamestate[rank][file-1].piece
                    if (temp.tostring() == "p" and temp.enpassant == True):
                        moves.append([rank, file-1])

        return moves

    

