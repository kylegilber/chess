from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.null import Null
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from board.square import Square

class Board:

    gamestate = [[0 for rank in range(8)] for file in range(8)]

    gamestate