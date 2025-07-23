from chessboard import Board

class Move:

    def __init__(self): pass

    def updatePosition(self, rank, file):
        pos = rank * 8 + file
        return pos

    def pinned(self, gamestate, legalMoves, rank, file, assoc):
        """
        :param gamestate: current chess board state
        :param legalMoves: list of a piece's moves
        :param rank: x coordinate of piece
        :param file: y coordinate of piece
        :returns: list of moves that do not result in a check on the king
        """

        moves = []
        temp = None
        for move in legalMoves:
            x, y = move[0], move[1]
            temp = gamestate[x][y].piece
            gamestate[x][y].piece = gamestate[rank][file].piece
            gamestate[rank][file].piece = Null()
            
            if (assoc == "Black"):
                if (len(self.checkB(gamestate)) == 0):
                    moves.append(move)
            else:
                if (len(self.checkW(gamestate)) == 0):
                    moves.append(move)

            gamestate[rank][file].piece = gamestate[x][y].piece
            gamestate[x][y].piece = temp

        return moves

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
        :param gamestate: current board state
        :returns: coordinates of piece checking the black king (if any)
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

    def checkW(self, gamestate):
        """
        :param gamestate: current board state
        :returns: coordinates of piece checking the white king
        """

        if (gamestate[7][4].piece.tostring() == "K"):
            rank, file = 7, 4
        else:
            for x in range(7, -1, -1):
                for y in range(7, -1, -1):
                    if (gamestate[x][y].piece.tostring() == "K"):
                        rank, file = x, y
                
        for x in range(7, -1, -1):
            for y in range(7, -1, -1):
                if (gamestate[x][y].piece.association == "Black"):
                    moves = gamestate[x][y].piece.legalMoves(gamestate)
                    
                    for move in moves:
                        if (move[0] == rank and move[1] == file):
                            return [x, y]
                        
        return []

    def movesInCheck(self, gamestate, assoc):
        """
        """

        moves = []
        temp = None

        for rank in range(8):
            for file in range(8):
                if (gamestate[rank][file].piece.association == assoc):
                    legalMoves = gamestate[rank][file].piece.legalMoves(gamestate)

                    for move in legalMoves:
                        x, y = move[0], move[1]
                        temp = gamestate[x][y].piece
                        gamestate[x][y].piece = gamestate[rank][file].piece
                        gamestate[rank][file].piece = Null()
                        gamestate[x][y].piece.position = self.updatePosition(x, y)

                        if (assoc == "Black"):
                            if (len(self.checkB(gamestate)) == 0):
                                moves.append([rank, file, x, y])
                                gamestate[rank][file].piece = gamestate[x][y].piece
                                gamestate[x][y].piece = temp
                                gamestate[rank][file].piece.position = self.updatePosition(rank, file)
                            else:
                                gamestate[rank][file].piece = gamestate[x][y].piece
                                gamestate[x][y].piece = temp
                                gamestate[rank][file].piece.position = self.updatePosition(rank, file)
                        else:
                            if (len(self.checkW(gamestate)) == 0):
                                moves.append([rank, file, x, y])
                                gamestate[rank][file].piece = gamestate[x][y].piece
                                gamestate[x][y].piece = temp
                                gamestate[rank][file].piece.position = self.updatePosition(rank, file)
                            else:
                                gamestate[rank][file].piece = gamestate[x][y].piece
                                gamestate[x][y].piece = temp
                                gamestate[rank][file].piece.position = self.updatePosition(rank, file)

        return moves


    def castleB(self, gamestate):
        """
        :param gamestate: current chess board state
        :returns: list of legal castling moves for the black king
        """

        moves = []
        if (gamestate[0][4].piece.tostring() == "k"):
            if (gamestate[0][4].piece.moved == False):
                if (gamestate[0][0].piece.tostring() == "r"):
                    if (gamestate[0][0].piece.moved == False):
                        if (gamestate[0][1].piece.association is None and
                            gamestate[0][2].piece.association is None and
                            gamestate[0][3].piece.association is None):
                            moves.append([0, 2])
                if (gamestate[0][7].piece.tostring() == "r"):
                    if (gamestate[0][7].piece.moved == False):
                        if (gamestate[0][6].piece.association is None and
                            gamestate[0][5].piece.association is None):
                            moves.append([0, 6])
        
        return moves
    
    def castleW(self, gamestate):
        """
        :param gamestate: current chess board state
        :returns: list of legal castling moves for the white king
        """

        moves = []
        if (gamestate[7][4].piece.tostring() == "K"):
            if (gamestate[7][4].piece.moved == False):
                if (gamestate[7][0].piece.tostring() == "R"):
                    if (gamestate[7][0].piece.moved == False):
                        if (gamestate[7][1].piece.association is None and
                            gamestate[7][2].piece.association is None and
                            gamestate[7][3].piece.associaiton is None):
                            moves.append([7, 2])
                if (gamestate[7][7].piece.tostring() == "R"):
                    if (gamestate[7][7].piece.moved == False):
                        if (gamestate[7][6].piece.association is None and
                            gamestate[7][5].piece.assocaition is None):
                            moves.append([7, 6])
        
        return moves
            
board = Board()
move = Move()
temp = move.getBit(board.rook, 0, 1)
print(temp)