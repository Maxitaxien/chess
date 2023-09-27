'''
CHESS

The general plan -
1: Create a main class for the pieces, divide this into subclasses for all the pieces.
2: Create a basic board (probably not too hard) and find a way to "place" pieces on this board.
3: Make the pieces able to make legal moves without allowing them to exit the board.
4: Make the pieces unable to step on squares where friendly pieces are situated.
5: Make the pieces able to capture enemy pieces.
6: Implement final checkmate and stalemate rules.

'''


from board import Board
from pieces import Piece


