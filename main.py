"""
CHESS

A program in which I will try to create the game of chess in Python.
The general plan -
1: Create pieces with associated methods - DONE
2: Create a basic board - DONE
3: Make the pieces able to make legal moves without allowing them to exit the board. - DONE
4: Make the pieces unable to step on squares where friendly pieces are situated. - DONE
5: Make the pieces able to capture enemy pieces. - DONE
6: Implement final checkmate and stalemate rules.
7: Implement special moves (castling, en passant)

After this: Using the game as a basis for a reinforcement learning agent?
"""

from board import Board
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
            move = input('Enter white\'s move in algebraic notation.')

        elif turn == -1:
            move = input('Enter black\'s move in algebraic notation.')

        if move.upper() == 'Q':
            confirm = input("Are you sure you want to end the game? Enter 'q' again to confirm, or anything else to cancel.").upper()
            if confirm == 'Q':
                break
            else:
                print('Resuming game.')
                continue

        #CHECKING VALIDITY OF MOVE

        if len(move) == 2:
            if move[-1] not in '12345678' or move[-2] not in 'abcdefgh':
                print('Invalid move entered, please try again.')
                continue

        elif len(move) == 3:
            if move[-1] not in '12345678' or move[-2] not in 'abcdefgh' or move[-3] not in 'RNBKQ':
                print('Invalid move entered, please try again.')
                continue

        # CHECK LEGALITY + MOVE PIECE IF LEGAL
        legal = board.legal_move(move, turn)

        if legal:
            print(f'{"White" if turn == 1 else "Black"} played {move}.')
        else:
            print('Illegal move entered, please try again.')
            continue

        board.show_board()

        turn_counter += 0.5
        turn *= -1

if __name__ == '__main__':
    main()
