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

After this: Using the game as a basis for a reinforcement learning agent?
"""

from board import Board
from pieces import *

def main():
    board = Board()
    board.setup()

    print("""Welcome to chess! Every move, enter a valid move in algebraic chess notation to continue the game,
    or enter 'Q' to quit. Here is the initial position:""")
    for row in reversed(board.board):
        print([str(piece) for piece in row])

    turn = 1 #Indicates white's turn
    turn_counter = 1


    while True: #MAIN GAME LOOP
        if turn == 1:
            move = input('Enter white\'s move in algebraic notation.').upper()

        elif turn == -1:
            move = input('Enter black\'s move in algebraic notation.').upper()

        if move == 'Q':
            break

        #CHECKING VALIDITY OF MOVE
        if len(move) == 2:
            if move[-1] not in '12345678' or move[-2] not in 'ABCDEFGH':
                print('Invalid move entered, please try again.')
                continue

        if len(move) == 3:
            if move[-1] not in '12345678' or move[-2] not in 'ABCDEFGH' or move[-3] not in 'RNBKQ':
                print('Invalid move entered, please try again.')
                continue

        #TODO: Implement legality check of move

        board.update(move, turn)

        for row in reversed(board.board):
            print([str(piece) for piece in row])

        turn_counter += 0.5
        turn *= -1

if __name__ == '__main__':
    main()