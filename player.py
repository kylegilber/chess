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
board.setupBoard()
board.printBoard()

# Colors
dark = (119, 149, 86)
light = (235, 236, 208)

playing = True
while playing:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            playing = False
            pygame.quit()

def renderSquare(color, w, h, x, y):
    """
    """

    pygame.draw.rect(
        surface= window,
        color= color,
        rect= [x, y, w, h]
    )
