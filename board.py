"""This program is for making a functional board.
This could have some general rules for the board - it restricts the pieces
to stay on the 1-8 coordinates in both the x and y direction.

Initially I will make the board as a standard Python matrix,
before experimenting with more exciting options later.

"""

from pieces import *

class Board():
    def __init__(self):
        self.board = [[EmptySquare() for row in range(8)] for col in range(8)]

    def setup(self): #Sets initial position.

        #PAWNS:
        self.board[1] = [Pawn(colour='W', pos=(1, col)) for col in range(8)]
        self.board[6] = [Pawn(colour='B', pos=(6, col)) for col in range(8)]

        #ROOKS
        self.board[0][0] = Rook(colour='W', pos=(0, 0))
        self.board[0][7] = Rook(colour='W', pos=(0, 7))

        self.board[7][0] = Rook(colour='B', pos=(7, 0))
        self.board[7][7] = Rook(colour='B', pos=(7, 7))

        #KNIGHTS
        self.board[0][1] = Knight(colour='W', pos=(0, 1))
        self.board[0][6] = Knight(colour='W', pos=(0, 6))

        self.board[7][1] = Knight(colour='B', pos=(7, 1))
        self.board[7][6] = Knight(colour='B', pos=(7, 6))

        #BISHOPS
        self.board[0][2] = Bishop(colour='W', pos=(0, 2))
        self.board[0][5] = Bishop(colour='W', pos=(0, 5))

        self.board[7][2] = Bishop(colour='B', pos=(7, 2))
        self.board[7][5] = Bishop(colour='B', pos=(7, 5))

        #QUEENS
        self.board[0][3] = Queen(colour='W', pos=(0, 3))

        self.board[7][3] = Queen(colour='B', pos=(7, 3))

        #KINGS
        self.board[0][4] = King(colour='W', pos=(0, 4))

        self.board[7][4] = King(colour='B', pos=(7,4))
    def update(self, move, turn):
        # Dictionary to convert 'ABCDEFGH' to numbers to update board
        col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        piece_dict = {'R': Rook(), 'N': Knight(), 'B': Bishop(), 'Q': Queen(), 'K': King()}

        if len(move) == 3:
            piece = piece_dict[move[0]]
            row = int(move[2]) - 1
            col = col_dict[move[1]]
        else:
            piece = Pawn()
            row = int(move[1]) - 1
            col = col_dict[move[0]]

        piece.colour = 'W' if turn > 0 else 'B'
        piece.pos = (row, col)

        self.board[row][col] = piece

        #TODO: Remove piece from previous position

