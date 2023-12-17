This is the start of a project to try and make chess from scratch on my own in python!

Current status: Movement and capture of all pieces should work correctly. Special rules like castling and en passant are not implemented, pawn promotion is not implemented and check/checkmate rules are not implemented.

File explanations:
The file pieces.py has all the piece classes with their associated methods.

The file board.py contains the Board classes with its main attribute Board.board which has a board representation. This file also has the logic for updating the board and checking for legal moves.

The file old_main.py contains the old game main loop that printed the bort as a nested list of string representations of the pieces.

The file main.py contains the main game loop with a simple tkinter graphical implementation.


To play the game as it is now, run the main.py file.