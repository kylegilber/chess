import pygame
from enum import Enum
from board.chessboard import Board
from board.move import Move

# Initialize pygame
pygame.init()

# Set window dimensions
window = pygame.display.set_mode((800, 800))

# Caption
pygame.display.set_caption("Chess")

# Clock
clock = pygame.time.Clock()

# Initialize chessboard
board = Board()
mover = Move()
board.setupBoard()
board.printBoard()

# Colors
dark = (119, 149, 86)
light = (235, 236, 208)
highlight = (247,245,125)

class Pieces(Enum):
    QUEEN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    NEXT = 4
    PAWN = 5

def renderSquare(color, x, y):
    pygame.draw.rect(
        surface= window,
        color= color,
        rect= [x, y, 100, 100]
    )

def renderBoard():
    x = y = temp = 0
    for rank in range(8):
        for file in range(8):
            if (temp % 2 == 0): renderSquare(light, x, y)
            else: renderSquare(dark, x, y)
            if (board.gamestate[rank][file].piece.tostring() != "-"):
                img = pygame.image.load("./assets/" + 
                    board.gamestate[rank][file].piece.tostring().lower() + 
                    board.gamestate[rank][file].piece.association[0].lower() +
                    ".svg")
                img = pygame.transform.scale(img, (100,100))
                window.blit(img, [x, y])
            x += 100
            temp += 1
        temp += 1
        y += 100
        x = 0

def getPosition(x, y):
    temp = x * 8
    pos = temp + y
    return pos

def isCheckmate(assoc):
    checks = mover.checkB(board.gamestate) if assoc == "Black" else mover.checkW(board.gamestate)
    if checks:
        moves = mover.movesInCheck(board.gamestate, assoc)
        return (len(moves) == 0)
    return False

def isStalemate(assoc):
    for rank in range(8):
        for file in range(8):
            piece = board.gamestate[rank][file].piece
            if (piece.association == assoc):
                moves = piece.legalMoves(board.gamestate)
                moves = mover.pinned(board.gamestate, moves, rank, file, assoc)
                if moves: return False
    return True

def isGameOver(turn):
    if (turn % 2 == 1):
        if (isCheckmate("Black")):
            return True, "White"
        if (isStalemate("Black")):
            return True, "Stalemate"
    else:
        if (isCheckmate("White")):
            return True, "Black"
        if (isStalemate("White")):
            return True, "Stalemate"
    return False, None

renderBoard()

## LOCAL

turn = 0
hist = []
promote = []
playing = True

while playing:
    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            playing = False
            pygame.quit()
            quit()
    
        if (event.type == pygame.MOUSEBUTTONDOWN):
            coord = pygame.mouse.get_pos()
            rank, file = coord[1] // 100, coord[0] // 100

            if (len(hist) == 0):
                playing, result = isGameOver(turn)

                color = "Black" if (turn % 2 == 1) else "White"
                func = mover.checkB if (color == "Black") else mover.checkW
                moves = mover.movesInCheck(board.gamestate, color) if (func(board.gamestate)) else None

                if moves:
                    for move in moves:
                        if (rank == move[0] and file == move[1]):
                            hist.append([move[2], move[3]])
                            break

            if promote:
                x, y = promote[Pieces.PAWN]
                pawn = board.gamestate[x][y].piece
                if (pawn.association == "Black"):
                    for piece, pos in enumerate(promote):
                        if (piece == Pieces.NEXT):
                            turn -= 1
                            break
                        if (pos[0] == rank and pos[1] == file):
                            choice = [Queen, Rook, Bishop, Knight][piece]
                            x, y = promote[Pieces.NEXT]
                            board.gamestate[x][y].piece = choice("Black", getPosition(x, y))
                            pawn = Null()
                            break

        pygame.display.update()