"""
CHESS

A program for the game of chess in Python.
The general plan -
1: Create pieces with associated methods - DONE
2: Create a basic board - DONE
3: Make the pieces able to make legal moves without allowing them to exit the board. - DONE
4: Make the pieces unable to step on squares where friendly pieces are situated. - DONE
5: Make the pieces able to capture enemy pieces. - DONE
6: Make some kind of graphics for the game - DONE (but under improvement)
7: Implement final checkmate, double and stalemate rules. - ONGOING
8: Implement special moves (castling, en passant, promotion - (especially important!))


After this: Using the game as a basis for a reinforcement learning agent?
"""

#TODO: ADD INSTRUCTIONS BUTTON THAT SHOWS INFO FROM INTRODUCTION IN old_main.py FILE.
#TODO: CHANGE PRINT STATEMENTS TO MESSAGES THAT SHOW UP IN TKINTER WINDOW

import tkinter as tk
from board import Board

def main():
    def handle_move(event=None):
        nonlocal turn
        nonlocal turn_counter
        valid = True
        double = False #Keeps track of if it is a "double" move (two pieces of the same type could move to the square)
        piece_abbrv = 'RNBKQ'
        col_abbrv = 'abcdefgh'
        row_abbrv = '12345678'

        move = entry.get()

        #There is surely a better way to do validity checking than exhaustively like this, but there are not that many cases to check for:

        if len(move) == 2: #Moves of the type "e5" are valid
            if move[-1] not in row_abbrv or move[-2] not in col_abbrv:
                valid = False
                print('Invalid move entered, please try again.')

        elif len(move) == 3: #Moves of the type "Qa5" are valid
            if move[-1] not in row_abbrv or move[-2] not in col_abbrv or move[-3] not in piece_abbrv:
                if move != '0-0':
                    valid = False
                    print('Invalid move entered, please try again.')

        elif len(move) == 4:
            if 'x' in move: #Moves of the type "axb4" or "Bxb4" are valid
                if move[-1] not in col_abbrv or move[-2] not in col_abbrv or move[0] not in col_abbrv + piece_abbrv:
                    valid = False
                    print('Invalid move entered, please try again')

            else: #Moves of the type "Nge2" and "N6g2" are valid
                if move[0] not in piece_abbrv or move[1] not in col_abbrv + row_abbrv or move [2] not in col_abbrv or move[3] not in row_abbrv:
                    valid = False
                    print('Invalid move entered, please try again.')
                else:
                    double = True

        elif len(move) == 5: #Moves of the type "Raxa6" are valid
            if 'x' not in move or move[0] not in piece_abbrv or move[1] not in col_abbrv + row_abbrv or move[2] != 'x'\
                    or move[3] not in col_abbrv or move[4] not in row_abbrv:
                if move != '0-0-0':
                    valid = False
                    print('Invalid move entered, please try again.')
            else:
                double = True
            #... or move != '0-0-0':

        else: #If 2 > len > 6, the move is never valid.
            valid = False
            print('Invalid move entered, please try again')

        if valid:
            legal, check = board.legal_move(move, turn, double=double)

            if legal:
                print(f'{"White" if turn == 1 else "Black"} played {move}.')
                if check:
                    show_check_message()
                turn *= -1
                board.draw_board(canvas)
                clear_entry()
                turn_counter += 0.5
            else:
                print('Illegal move entered, please try again.')

    def show_check_message():
        x_entry, y_entry = entry.winfo_x(), entry.winfo_y()
        check_label.place(x=x_entry - 80, y=y_entry, anchor=tk.NE)
        root.after(3000, check_label.place_forget)
    def clear_entry():
        entry.delete(0, tk.END)  #Clears text entry field

    board = Board()
    board.setup()

    turn = 1
    turn_counter = 1

    root = tk.Tk()
    root.title("Chess")

    canvas = tk.Canvas(root, width=680, height=700)
    canvas.pack()

    entry_var = tk.StringVar()

    entry = tk.Entry(root, textvariable=entry_var)
    entry.bind("<Return>", handle_move)

    entry.pack()

    submit_button = tk.Button(root, text='Submit Move', command=handle_move)
    submit_button.pack()

    check_label = tk.Label(root, text='Check!', font=('Times New Roman', 18), bg='white')

    board.draw_board(canvas)

    root.mainloop()

if __name__ == '__main__':
    main()
