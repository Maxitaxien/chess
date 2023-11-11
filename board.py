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
        self.col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.col_dict_rev = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

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
        self.white_pieces['Q'] = queens_w #Although we only have one queen to start with, we could promote later!

        queens_b = [Queen(colour='B', pos=(7, 3))]
        self.board[7][3] = queens_b[0]
        self.black_pieces['Q'] = queens_b


        #KINGS
        kings_w = [King(colour='W', pos=(0, 4))]
        self.board[0][4] = kings_w[0]
        self.white_pieces['K'] = kings_w #Ok, we will definitely never have more than one king... but let's just stay consistent

        kings_b = [King(colour='B', pos=(7, 4))]
        self.board[7][4] = kings_b[0]
        self.black_pieces['K'] = kings_b

    def show_board(self):
        #TODO: Implement functionality to show board without "reversed" for the black view.
        for row in reversed(self.board):
            print([str(piece) for piece in row])

    def update(self, piece, move, colour):
        # Dictionary to convert 'ABCDEFGH' to numbers to update board
        piece_dict = {'R': Rook(), 'N': Knight(), 'B': Bishop(), 'Q': Queen(), 'K': King()}

        row = int(move[-1]) - 1
        col = self.col_dict[move[-2]]
        piece.pos = (row, col)

        self.board[row][col] = piece

        if 'X' in move: #CAPTURE
            if colour == 1:
                piece_dict = self.black_pieces
            else:
                piece_dict = self.white_pieces

            for key, value in piece_dict.items():
                for p in value:
                    if p.pos == piece.pos:
                        value.remove(p)




    def calc_diagonal(self, piece):
        # UP AND LEFT
        row = piece.pos[0] + 1
        col = piece.pos[1] + 1
        if row < 8 and col < 8:
            while (7 >= row) and (7 >= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row += 1
                col += 1
            if (7 >= row) and (7 >= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        # DOWN AND RIGHT
        row = piece.pos[0] - 1
        col = piece.pos[1] - 1

        if row >= 0 and col >= 0:
            while (0 <= row) and (0 <= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row -= 1
                col -= 1
            if (0 <= row) and (0 <= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        # UP AND RIGHT
        row = piece.pos[0] + 1
        col = piece.pos[1] - 1

        if row < 8 and col >= 0:
            while (7 >= row) and (0 <= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row += 1
                col -= 1
            if (7 >= row) and (0 <= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        # DOWN AND LEFT
        row = piece.pos[0] - 1
        col = piece.pos[1] + 1

        if row >= 0 and col < 8:
            while (0 <= row) and (7 >= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row -= 1
                col += 1
            if (0 <= row) and (7 >= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

    def calc_cardinal(self, piece):

        #Finding possible vertical rules:
        row = piece.pos[0] + 1
        col = piece.pos[1]
        if row < 8:
            while (7 >= row) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row += 1
            if (7 >= row) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        row = piece.pos[0] - 1

        if row >= 0:
            while (0 <= row) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                row -= 1
            if (0 <= row) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        # Finding possible horizontal moves:
        row = piece.pos[0]
        col = piece.pos[1] + 1
        if col < 8:
            while (7 >= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                col += 1
            if (7 >= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        col = piece.pos[1] - 1

        if col >= 0:
            while (0 <= col) and isinstance(self.board[row][col], EmptySquare):
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)
                col -= 1
            if (0 <= col) and self.board[row][col].colour != piece.colour:
                coords_converted = (self.col_dict_rev[col], str((row) + 1))
                move_converted = str(piece)[0] + 'x' + ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

    def legal_move(self, move, colour):
        piece_to_move = None
        legal = False

        if colour == 1:
            checking_dict = self.white_pieces
        else:
            checking_dict = self.black_pieces

        #PAWN
        #TODO: For pawns, it makes sense to only check pawns on the same column. This is a possible optimization for the program.
        if move[0] not in 'NBRQK':
            for pawn in checking_dict['P']: #Check every pawn
                potential_moves = []
                basic_move = (1, 0) if colour == 1 else (-1, 0) #Black moves down the board, white moves up
                starting_move = (2, 0) if colour == 1 else (-2, 0)


                potential_moves.append(basic_move)

                if (colour == -1 and pawn.pos[0] == 6) or (colour == 1 and pawn.pos[0] == 1):
                    potential_moves.append(starting_move)

                square_front = [pawn.pos[0] + 1, pawn.pos[1]] if colour == 1 else [pawn.pos[0] - 1, pawn.pos[1]]

                #CHECKING IF NORMAL MOVES ARE LEGAL
                for potential_move in potential_moves:
                    pos_after_move = (pawn.pos[0] + potential_move[0], pawn.pos[1])
                    if isinstance(self.board[square_front[0]][square_front[1]], EmptySquare) and ((7 >= square_front[0]) >= 0) and (7 >= square_front[1] >= 0):
                        coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                        move_converted = ''.join(coords_converted)
                        pawn.legal_moves.append(move_converted)

                #CHECKING IF CAPTURES ARE LEGAL
                captures = [(1, 1) if colour == 1 else (-1, 1), (1, -1) if colour == 1 else (-1, -1)]
                for capture in captures:
                    pos_after_move = (pawn.pos[0] + capture[0], pawn.pos[1] + capture[1])
                    if ((7 >= pos_after_move[0]) >= 0) and (7 >= pos_after_move[1] >= 0) and not(isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare)) and self.board[pos_after_move[0]][pos_after_move[1]].colour != pawn.colour:
                        coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                        move_converted = self.col_dict_rev[pawn.pos[1]] + 'x' + ''.join(coords_converted)
                        pawn.legal_moves.append(move_converted)

            for pawn in checking_dict['P']:
                if move in pawn.legal_moves:
                    legal = True

                    last_row = pawn.pos[0]
                    last_col = pawn.pos[1]

                    if colour == 1:
                        pawn.pos = (pawn.pos[0] + (int(move[-1]) - 1), pawn.pos[1] - int(self.col_dict[move[-2]]))
                        self.white_pieces['P'] = [pawn for pawn in checking_dict['P']]
                    else:
                        pawn.pos = (pawn.pos[0] - (int(move[-1]) - 1), pawn.pos[1] - int(self.col_dict[move[-2]]))
                        self.black_pieces['P'] = [pawn for pawn in checking_dict['P']]

                    self.update(pawn, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                pawn.legal_moves = []  # Reset legal moves

        #ROOK
        elif move[0] == 'R':
            for rook in checking_dict['R']:
                self.calc_cardinal(rook)

            for rook in checking_dict['R']:
                if move in rook.legal_moves:
                    legal = True

                    last_row = rook.pos[0]
                    last_col = rook.pos[1]

                    if colour == 1:
                        rook.pos = (rook.pos[0] + (int(move[-1]) - 1), rook.pos[1] - int(self.col_dict[move[-2]]))
                        self.white_pieces['R'] = [rook for rook in checking_dict['R']]
                    else:
                        rook.pos = (rook.pos[0] - (int(move[-1]) - 1), rook.pos[1] - int(self.col_dict[move[-2]]))
                        self.black_pieces['R'] = [rook for rook in checking_dict['R']]

                    self.update(rook, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                rook.legal_moves = []  # Reset legal moves

        #KNIGHT
        elif move[0] == 'N':
            for knight in checking_dict['N']:
                potential_moves = [(2, 1), (2, -1), (-2, 1), (-2,-1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

                for potential_move in potential_moves:
                    pos_after_move = (knight.pos[0] + potential_move[0], knight.pos[1] + potential_move[1])
                    if (7 >= pos_after_move[0] >= 0) and (7 >= pos_after_move[1] >= 0):
                        if isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare):
                            coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                            move_converted = 'N' + ''.join(coords_converted)
                            knight.legal_moves.append(move_converted)
                        elif self.board[pos_after_move[0]][pos_after_move[1]].colour != knight.colour:
                            coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                            move_converted = 'N' + 'x' + ''.join(coords_converted)
                            knight.legal_moves.append(move_converted)



            for knight in checking_dict['N']:
                if move in knight.legal_moves:
                    legal = True

                    last_row = knight.pos[0]
                    last_col = knight.pos[1]

                    if colour == 1:
                        knight.pos = (knight.pos[0] + (int(move[-1]) - 1), knight.pos[1] - int(self.col_dict[move[-2]]))
                        self.white_pieces['N'] = [knight for knight in checking_dict['N']]
                    else:
                        knight.pos = (knight.pos[0] - (int(move[-1]) - 1), knight.pos[1] - int(self.col_dict[move[-2]]))
                        self.black_pieces['N'] = [knight for knight in checking_dict['N']]

                    self.update(knight, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                knight.legal_moves = []  # Reset legal moves


        #BISHOP
        elif move[0] == 'B':
            for bishop in checking_dict['B']:

                self.calc_diagonal(bishop)

                for bishop in checking_dict['B']:
                    if move in bishop.legal_moves:
                        legal = True

                        last_row = bishop.pos[0]
                        last_col = bishop.pos[1]

                        if colour == 1:
                            bishop.pos = (bishop.pos[0] + (int(move[-1]) - 1), bishop.pos[1] - int(self.col_dict[move[-2]]))
                            self.white_pieces['B'] = [bishop for bishop in checking_dict['B']]
                        else:
                            bishop.pos = (bishop.pos[0] - (int(move[-1]) - 1), bishop.pos[1] - int(self.col_dict[move[-2]]))
                            self.black_pieces['B'] = [bishop for bishop in checking_dict['B']]

                        self.update(bishop, move, colour)

                        self.board[last_row][last_col] = EmptySquare()

                    bishop.legal_moves = []  # Reset legal moves

        #QUEEN
        elif move[0] == 'Q':
            for queen in checking_dict['Q']:

                self.calc_cardinal(queen)
                self.calc_diagonal(queen)

            for queen in checking_dict['Q']:
                if move in queen.legal_moves:
                    legal = True

                    last_row = queen.pos[0]
                    last_col = queen.pos[1]

                    if colour == 1:
                        queen.pos = (queen.pos[0] + (int(move[-1]) - 1), queen.pos[1] - int(self.col_dict[move[-2]]))
                        self.white_pieces['Q'] = [queen for queen in checking_dict['Q']]
                    else:
                        queen.pos = (queen.pos[0] - (int(move[-1]) - 1), queen.pos[1] - int(self.col_dict[move[-2]]))
                        self.black_pieces['Q'] = [queen for queen in checking_dict['Q']]

                    self.update(queen, move, colour)

                    self.board[last_row][last_col] = EmptySquare()

                queen.legal_moves = []  # Reset legal moves


        #KING
        elif move[0] == 'K' or move == '0-0' or move == '0-0-0':
            #TODO: Implement castling move
            #TODO: Make attacked squares off-limits - that is, calculate all legal moves for opponent's pieces and see if they match new coords
            #(This means you should probably put all the calculations in their own functions anyway)

            for king in checking_dict['K']: #There will only ever be one king, but let's stay consistent with the rest of the program
                potential_moves = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

                for potential_move in potential_moves:
                    pos_after_move = (king.pos[0] + potential_move[0], king.pos[1] + potential_move[1])
                    if (7 >= pos_after_move[0] >= 0) and (7 >= pos_after_move[1] >= 0):
                        if isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare):
                            coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                            move_converted = 'K' + ''.join(coords_converted)
                            king.legal_moves.append(move_converted)
                        elif self.board[pos_after_move[0]][pos_after_move[1]].colour != king.colour:
                            coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                            move_converted = 'K' + 'x' + ''.join(coords_converted)
                            king.legal_moves.append(move_converted)


                for king in checking_dict['K']:
                    if move in king.legal_moves:
                        legal = True

                        last_row = king.pos[0]
                        last_col = king.pos[1]

                        if colour == 1:
                            king.pos = (king.pos[0] + (int(move[-1]) - 1), king.pos[1] - int(self.col_dict[move[-2]]))
                            self.white_pieces['K'] = [king for king in checking_dict['K']]
                        else:
                            king.pos = (king.pos[0] - (int(move[-1]) - 1), king.pos[1] + int(self.col_dict[move[-2]]))
                            self.black_pieces['K'] = [king for king in checking_dict['K']]

                        self.update(king, move, colour)

                        self.board[last_row][last_col] = EmptySquare()

                    king.legal_moves = []  # Reset legal moves

        return legal