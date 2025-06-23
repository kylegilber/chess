from pieces.null import Null

class Move:

    def __init__(self): pass


    def updatePosition(self, rank, file):
        pos = rank * 8 + file
        return pos

    def enpassant(self, gamestate, rank, file):
        """
        :param gamestate: current board state
        :param rank: rank to check for a pawn
        :param file: file to check for a pawn
        :returns: list of legal en passant moves
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

    def checkB(self, gamestate):
        """
        """
        
        if (gamestate[0][4].piece.tostring() == "k"): 
            rank, file = 0, 4
        else:
            for x in range(8):
                for y in range(8):
                    if (gamestate[x][y].piece.tostring() == "k"):
                        rank, file = x, y
        
        for x in range(8):
            for y in range(8):
                if (gamestate[x][y].piece.association == "White"):
                    moves = gamestate[x][y].piece.legalMoves(gamestate)
                    for move in moves:
                        if (move[0] == rank and move[1] == file):
                            return [x, y]
        return []


