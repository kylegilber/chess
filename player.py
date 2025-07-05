import pygame
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
move = Move()
board.setupBoard()
board.printBoard()

# Colors
dark = (119, 149, 86)
light = (235, 236, 208)

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

def isCheckmate(assoc):
    checks = move.checkB(board.gamestate) if assoc == "Black" else move.checkW(board.gamestate)
    if checks:
        moves = move.movesInCheck(board.gamestate, assoc)
        return (len(moves) == 0)
    return False

def isStalemate(assoc):
    for rank in range(8):
        for file in range(8):
            piece = board.gamestate[rank][file].piece
            if (piece.association == assoc):
                moves = piece.legalMoves(board.gamestate)
                moves = move.pinned(board.gamestate, moves, rank, file, assoc)
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
moves = []
playing = True

while playing:
    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            playing = False
            pygame.quit()
            quit()
    
        if (len(moves) == 0):
            playing, result = isGameOver(turn)

        pygame.display.update()