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

def ischeckmate(assoc):
    if (assoc == "Black"):
        checks = move.checkB(board.gamestate)
    else: checks = move.checkW(board.gamestate)

    if (len(checks) != 0):
        moves = move.movesInCheck(board.gamestate, assoc)
        if (len(moves) == 0): 
            return True
    return False



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
            if (turn % 2 == 1):
                if (ischeckmate("Black")):
                    playing = False
                    result = "White"
            else:
                if (ischeckmate("White")):
                    playing = False
                    result = "Black"

                else:
                    check = False
                    for rank in range(8):
                        for file in range(8):
                            if (board.gamestate[rank][file].piece.association == "Black"):
                                movesl = board.gamestate[rank][file].piece.legalMoves(board.gamestate)
                                temp = move.pinned(board.gamestate, movesl, rank, file, "Black")
                                if (len(temp) == 0): continue
                                else:
                                    check = True
                                    break
                        if (check): break

                    if not check: 
                        playing = False
                        result = "Stalemate"
            else:
                if (len(move.checkW(board.gamestate)) != 0):
                    if (len(move.movesInCheck(board.gamestate, "White")) == 0):
                        playing = False
                        result = "Black"
                else:
                    check = False
                    for rank in range(8):
                        for file in range(8):
                            if (board.gamestate[rank][file].piece.association == "White"):
                                movesl = board.gamestate[rank][file].piece.legalMoves(board.gamestate)
                                temp = move.pinned(board.gamestate, movesl, rank, file, "White")
                                if (len(temp) == 0): continue
                                else:
                                    check = True
                                    break
                        if (check): break

                    if not check: 
                        playing = False
                        result = "Stalemate"

        pygame.display.update()