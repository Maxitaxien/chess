"""
CHESS

A program in which I will try to create the game of chess in Python.
The general plan -
1: Create pieces with associated methods
2: Create a basic board
3: Make the pieces able to make legal moves without allowing them to exit the board.
4: Make the pieces unable to step on squares where friendly pieces are situated.
5: Make the pieces able to capture enemy pieces.
6: Implement final checkmate and stalemate rules.

Contiuining: Using the game as a basis for a reinforcement learning agent?
"""


from board import Board
from pieces import *

board = Board()

board.setup()

board = Board()
board.setup()
for row in board.board:
    print(row)

board.update
pawns = Pawn('W', [0,0])