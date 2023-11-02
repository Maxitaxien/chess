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
        self.white_pieces = {}
        self.black_pieces = {}
        self.col_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.col_dict_rev = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

    def setup(self): #Sets initial position and pieces to piece dictionaries

        #PAWNS:
        pawns_w = [Pawn(colour='W', pos=(1, col)) for col in range(8)]
        self.white_pieces['P'] = pawns_w
        self.board[1] = pawns_w

        pawns_b = [Pawn(colour='B', pos=(6, col)) for col in range(8)]
        self.black_pieces['P'] = pawns_b
        self.board[6] = pawns_b

        #ROOKS
        rooks_w = [Rook(colour='W', pos=(0, 0)), Rook(colour='W', pos=(0,7))]
        self.board[0][0] = rooks_w[0]
        self.board[0][7] = rooks_w[1]
        self.white_pieces['R'] = rooks_w

        rooks_b = [Rook(colour='B', pos=(7, 0)), Rook(colour='B', pos=(7, 7))]
        self.board[7][0] = rooks_b[0]
        self.board[7][7] = rooks_b[1]
        self.black_pieces['R'] = rooks_b

        #KNIGHTS
        knights_w = [Knight(colour='W', pos=(0, 1)), Knight(colour='W', pos=(0, 6))]
        self.board[0][1] = knights_w[0]
        self.board[0][6] = knights_w[1]
        self.white_pieces['N'] = knights_w

        knights_b = [Knight(colour='B', pos=(7, 1)), Knight(colour='B', pos=(7, 6))]
        self.board[7][1] = knights_b[0]
        self.board[7][6] = knights_b[1]
        self.black_pieces['N'] = knights_b

        #BISHOPS
        bishops_w = [Bishop(colour='W', pos=(0, 2)), Bishop(colour='W', pos=(0, 5))]
        self.board[0][2] = bishops_w[0]
        self.board[0][5] = bishops_w[1]
        self.white_pieces['B'] = bishops_w

        bishops_b = [Bishop(colour='B', pos=(7, 2)), Bishop(colour='B', pos=(7, 5))]
        self.board[7][2] = bishops_b[0]
        self.board[7][5] = bishops_b[1]
        self.black_pieces['B'] = bishops_b

        #QUEENS
        queens_w = [Queen(colour='W', pos=(0, 3))]
        self.board[0][3] = queens_w[0]

        queens_b = [Queen(colour='B', pos=(7, 3))]
        self.board[7][3] = queens_b[0]

        #KINGS
        kings_w = [King(colour='W', pos=(0, 4))]
        self.board[0][4] = kings_w[0]

        kings_b = [King(colour='B', pos=(7, 4))]
        self.board[7][4] = kings_b[0]

    def show_board(self):
        for row in reversed(self.board): #Note: You could have a show_board without reversed for the black side to flip view around.
            print([str(piece) for piece in row])

    def update(self, piece, move, colour):
        # Dictionary to convert 'ABCDEFGH' to numbers to update board
        piece_dict = {'R': Rook(), 'N': Knight(), 'B': Bishop(), 'Q': Queen(), 'K': King()}

        if len(move) == 3: #ALL OTHER THAN PAWNS
            row = int(move[2]) - 1
            col = self.col_dict[move[1]]

            piece.pos = (row, col)

        else: #PAWN MOVE
            row = int(move[1]) - 1
            col = self.col_dict[move[0]]

            piece.pos = (row, col)

        if colour == 1:
            pass


        self.board[row][col] = piece

    def check_legality(self, move, colour):
        piece_to_move = None
        legal = False

        if colour == 1:
            checking_dict = self.white_pieces
        else:
            checking_dict = self.black_pieces

        #PAWN
        #TODO: For pawns, it makes sense to only check pawns on the same column. This is a possible optimization for the program.
        if move[0] not in 'NRBQK': #If first coordinate of move is not a piece, then it is a pawn
            for pawn in checking_dict['P']: #Check every pawn
                potential_moves = []
                basic_move = (1, 0) if colour == 1 else (-1, 0) #Black moves down the board, white moves up
                starting_move = (2, 0) if colour == 1 else (-2, 0)

                potential_moves.append(basic_move)

                if (colour == -1 and pawn.pos[0] == 6) or (colour == 1 and pawn.pos[0] == 1):
                    potential_moves.append(starting_move)

                square_front = [pawn.pos[0] + 1, pawn.pos[1]] if colour == 1 else [pawn.pos[0] - 1, pawn.pos[1]]

                for potential_move in potential_moves:
                    pos_after_move = (pawn.pos[0] + potential_move[0], pawn.pos[1])
                    if isinstance(self.board[square_front[0]][square_front[1]], EmptySquare) and ((7 >= square_front[0]) >= 0) and (7 >= square_front[1] >= 0):
                        coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                        move_converted = ''.join(coords_converted)
                        pawn.legal_moves.append(move_converted)

            for pawn in checking_dict['P']:
                if move in pawn.legal_moves:
                    legal = True

                    last_row = pawn.pos[0]
                    last_col = pawn.pos[1]

                    if colour == 1:
                        pawn.pos = (pawn.pos[0] + (int(move[1]) - 1), pawn.pos[1])
                        self.white_pieces['P'] = [pawn for pawn in checking_dict['P']]
                    else:
                        pawn.pos = (pawn.pos[0] - (int(move[1]) - 1), pawn.pos[1])
                        self.black_pieces['P'] = [pawn for pawn in checking_dict['P']]

                    self.update(pawn, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                pawn.legal_moves = []  # Reset legal moves

        #ROOK
        elif move[0] == 'R':
            for rook in checking_dict['R']:
                legal_moves = []

                #Finding possible vertical moves:
                row = rook.pos[0] + 1
                col = rook.pos[1]
                if row < 8:
                    while isinstance(self.board[row][col], EmptySquare) and (6 >= row):
                        coords_converted = (self.col_dict_rev[col], str((row) + 1))
                        move_converted = 'R' + ''.join(coords_converted)
                        rook.legal_moves.append(move_converted)
                        row += 1

                row = rook.pos[0] - 1

                if row >= 0:
                    while isinstance(self.board[row][col], EmptySquare) and (0 <= row):
                        coords_converted = (self.col_dict_rev[col], str((row) + 1))
                        move_converted = 'R' + ''.join(coords_converted)
                        rook.legal_moves.append(move_converted)
                        row -= 1

                #Finding possible horizontal moves
                row = rook.pos[0]
                col = rook.pos[1] + 1
                if col < 8:
                    while isinstance(self.board[row][col], EmptySquare) and (6 >= col):
                        coords_converted = (self.col_dict_rev[col], str((row) + 1))
                        move_converted = 'R' + ''.join(coords_converted)
                        rook.legal_moves.append(move_converted)
                        col += 1

                col = rook.pos[1] - 1

                if col >= 0:
                    while isinstance(self.board[row][col], EmptySquare) and (0 <= col):
                        coords_converted = (self.col_dict_rev[col], str((row) + 1))
                        move_converted = 'R' + ''.join(coords_converted)
                        rook.legal_moves.append(move_converted)
                        col -= 1

            for rook in checking_dict['R']:
                if move in rook.legal_moves:
                    legal = True

                    last_row = rook.pos[0]
                    last_col = rook.pos[1]

                    if colour == 1:
                        rook.pos = (rook.pos[0] + (int(move[2]) - 1), rook.pos[1])
                        self.white_pieces['R'] = [rook for rook in checking_dict['R']]
                    else:
                        rook.pos = (rook.pos[0] - (int(move[2]) - 1), rook.pos[1])
                        self.black_pieces['R'] = [rook for rook in checking_dict['R']]

                    self.update(rook, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                rook.legal_moves = []  # Reset legal moves

        #KNIGHT
        elif move[0] == 'N':
            return

        #BISHOP
        elif move[0] == 'B':
            return

        #QUEEN
        elif move[0] == 'Q':
            return

        #KING
        elif move[0] == 'K':
            return

        return legal