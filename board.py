"""This program is for making a functional board.
This could have some general rules for the board - it restricts the pieces
to stay on the 1-8 coordinates in both the x and y direction.

Initially I will make the board as a standard Python matrix,
before experimenting with more exciting options later.

"""

from pieces import *

class Board():
    def __init__(self):
        self.board = [['0_0' for _ in range(8)] for _ in range(8)]
    def setup(self): #Sets initial position.
        #Placeholder strings for now - piece objects later

        #PAWNS:
        self.board[1] = ['P_B' for _ in range(8)]
        self.board[6] = ['P_W' for _ in range(8)]

        #ROOKS
        self.board[0][0] = 'R_B'
        self.board[0][7] = 'R_B'

        self.board[7][0] = 'R_W'
        self.board[7][7] = 'R_W'

        #KNIGHTS
        self.board[0][1] = 'N_B'
        self.board[0][6] = 'N_B'

        self.board[7][1] = 'N_W'
        self.board[7][6] = 'N_W'

        #BISHOPS
        self.board[0][2] = 'B_B'
        self.board[0][5] = 'B_B'

        self.board[7][2] = 'B_W'
        self.board[7][5] = 'B_W'

        #QUEENS
        self.board[0][3] = 'Q_B'

        self.board[7][3] = 'Q_W'

        #KINGS
        self.board[0][4] = 'K_B'

        self.board[7][4] = 'K_W'
    def update(self):
        pass

