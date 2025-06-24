import pygame
from board.chessboard import Board

# Initialize pygame
pygame.init()

# Set display size
gameDisplay = pygame.display.set_mode((800, 800))

# Caption
pygame.display.set_caption("Chess")

# Clock
clock = pygame.time.Clock()

# Initialize chessboard
board = Board()
board.setupBoard()
board.printBoard()

