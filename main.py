"""CHESS

A program for the game of chess in Python.
The general plan -
1: Create pieces with associated methods - DONE
2: Create a basic board - DONE
3: Make the pieces able to make legal moves without allowing them to exit the board. - DONE
4: Make the pieces unable to step on squares where friendly pieces are situated. - DONE
5: Make the pieces able to capture enemy pieces. - DONE
6: Implement final checkmate and stalemate rules. - ONGOING
7: Implement special moves (castling, en passant, promotion - (especially important!))
8: Make some kind of graphics for the game

After this: Using the game as a basis for a reinforcement learning agent?
"""

#TODO: ADD INSTRUCTIONS BUTTON THAT SHOWS INFO FROM INTRODUCTION IN old_main.py FILE.

import tkinter as tk
from board import Board

def main():
    def handle_move(event=None):
        nonlocal turn
        nonlocal turn_counter

        move = entry.get()

        if len(move) == 2:
            if move[-1] not in '12345678' or move[-2] not in 'abcdefgh':
                print('Invalid move entered, please try again.')

        elif len(move) == 3:
            if move[-1] not in '12345678' or move[-2] not in 'abcdefgh' or move[-3] not in 'RNBKQ':
                print('Invalid move entered, please try again.')

        elif len(move) == 4:
            pass #TODO: IMPLEMENT LOGIC TO CHECK IF IT IS A CAPTURE (Rxe4) OR A "DOUBLE" MOVE (Raa6, R2a6)

        #TODO: DO THE SAME FOR MOVES OF LEN 5
        #TODO: SET SPECIAL FLAG FOR THESE MOVES, ALLOW FLAG IN board.legal_move AND IN THESE CASES ONLY MOVE THE PIECE THAT MATCHES

        legal, check = board.legal_move(move, turn)

        if legal:
            print(f'{"White" if turn == 1 else "Black"} played {move}.')
            if check:
                show_check_message()
            turn *= -1
            board.draw_board(canvas)
            clear_entry()
            turn_counter += +0.5
        else:
            print('Illegal move entered, please try again.')

    def show_check_message():
        x_entry, y_entry = entry.winfo_x(), entry.winfo_y()
        check_label.place(x=x_entry - 80, y=y_entry, anchor=tk.NE)
        root.after(2000, check_label.place_forget)
    def clear_entry():
        entry.delete(0, tk.END)  #Clears text entry field

    board = Board()
    board.setup()

    turn = 1
    turn_counter = 1

    root = tk.Tk()
    root.title("Chess")

    canvas = tk.Canvas(root, width=640, height=640)
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
