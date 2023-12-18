"""This program is for making a functional board.
This could have some general rules for the board - it restricts the pieces
to stay on the 1-8 coordinates in both the x and y direction.

Initially I will make the board as a standard Python nested list,
before experimenting with more exciting/better looking options later.

"""

from pieces import *
import tkinter as tk

class Board():
    def __init__(self):
        self.board = [[EmptySquare() for row in range(8)] for col in range(8)]
        self.white_pieces = {}
        self.black_pieces = {}

        #Dictionaries for translating algebraic chess notation to board coordinates
        self.col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        self.col_dict_rev = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def setup(self): #Sets initial position and pieces to piece dictionaries

        #PAWNS:
        pawns_w = [Pawn(colour=1, pos=(1, col)) for col in range(8)]
        self.white_pieces['P'] = pawns_w
        self.board[1] = pawns_w

        pawns_b = [Pawn(colour=0, pos=(6, col)) for col in range(8)]
        self.black_pieces['P'] = pawns_b
        self.board[6] = pawns_b

        #ROOKS
        rooks_w = [Rook(colour=1, pos=(0, 0)), Rook(colour=1, pos=(0,7))]
        self.board[0][0] = rooks_w[0]
        self.board[0][7] = rooks_w[1]
        self.white_pieces['R'] = rooks_w

        rooks_b = [Rook(colour=0, pos=(7, 0)), Rook(colour=0, pos=(7, 7))]
        self.board[7][0] = rooks_b[0]
        self.board[7][7] = rooks_b[1]
        self.black_pieces['R'] = rooks_b

        #KNIGHTS
        knights_w = [Knight(colour=1, pos=(0, 1)), Knight(colour=1, pos=(0, 6))]
        self.board[0][1] = knights_w[0]
        self.board[0][6] = knights_w[1]
        self.white_pieces['N'] = knights_w

        knights_b = [Knight(colour=0, pos=(7, 1)), Knight(colour=0, pos=(7, 6))]
        self.board[7][1] = knights_b[0]
        self.board[7][6] = knights_b[1]
        self.black_pieces['N'] = knights_b

        #BISHOPS
        bishops_w = [Bishop(colour=1, pos=(0, 2)), Bishop(colour=1, pos=(0, 5))]
        self.board[0][2] = bishops_w[0]
        self.board[0][5] = bishops_w[1]
        self.white_pieces['B'] = bishops_w

        bishops_b = [Bishop(colour=0, pos=(7, 2)), Bishop(colour=0, pos=(7, 5))]
        self.board[7][2] = bishops_b[0]
        self.board[7][5] = bishops_b[1]
        self.black_pieces['B'] = bishops_b

        #QUEENS
        queens_w = [Queen(colour=1, pos=(0, 3))]
        self.board[0][3] = queens_w[0]
        self.white_pieces['Q'] = queens_w #Although we only have one queen to start with, we could promote later!

        queens_b = [Queen(colour=0, pos=(7, 3))]
        self.board[7][3] = queens_b[0]
        self.black_pieces['Q'] = queens_b


        #KINGS
        kings_w = [King(colour=1, pos=(0, 4))]
        self.board[0][4] = kings_w[0]
        self.white_pieces['K'] = kings_w #Ok, we will definitely never have more than one king... but let's just stay consistent

        kings_b = [King(colour=0, pos=(7, 4))]
        self.board[7][4] = kings_b[0]
        self.black_pieces['K'] = kings_b

    #NOTE: The following function is heavily inspired by output from ChatGPT
    def draw_board(self, canvas):
        square_size = 80
        colors = ["white", "grey"]
        margin = 20  # Define a margin to leave space for labels

        for i in range(8):
            for j in range(8):
                x0, y0 = j * square_size + margin, i * square_size + margin
                x1, y1 = x0 + square_size, y0 + square_size
                color = colors[(i + j) % 2]

                canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                canvas.create_text(x0 + square_size / 2, y0 + square_size / 2,
                                   text=self.board[7 - i][j], font=('Times New Roman', 54))

        #A-H top
        for col in range(8):
            canvas.create_text(margin + square_size / 2 + col * square_size, margin / 2,
                               text=chr(65 + col), font=("Arial", 12), anchor=tk.CENTER)

        #A-H bottom
        for col in range(8):
            canvas.create_text(margin + square_size / 2 + col * square_size, margin*2 + 8 * square_size,
                               text=chr(65 + col), font=("Arial", 12), anchor=tk.CENTER)

        #1-8 left
        for row in range(8):
            canvas.create_text(margin / 2, margin + square_size / 2 + row * square_size,
                                text=str(8 - row), font=("Arial", 12), anchor=tk.CENTER)

        #1-8 right
        for row in range(8):
            canvas.create_text(margin * 1.5 + square_size * 8, margin + square_size / 2 + row * square_size,
                               text=str(8 - row), font=("Arial", 12), anchor=tk.CENTER)

        canvas.create_rectangle(margin, margin, margin + 8 * square_size, margin + 8 * square_size,
                                outline="black", width=2)

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

    def calc_threats(self, colour):
        threatened_squares = set()

        opposing_dict = self.black_pieces if colour == 1 else self.white_pieces

        for pawn in opposing_dict['P']:
            squares = self.calc_pawn(pawn, for_king=True)
            threatened_squares.update(squares)
        for knight in opposing_dict['N']:
            squares = self.calc_knight(knight, for_king=True)
            threatened_squares.update(squares)
        for bishop in opposing_dict['B']:
            squares = self.calc_diagonal(bishop, for_king=True)
            threatened_squares.update(squares)
        for rook in opposing_dict['R']:
            squares = self.calc_cardinal(rook, for_king=True)
            threatened_squares.update(squares)
        for queen in opposing_dict['Q']:
            squares1 = self.calc_cardinal(queen, for_king=True)
            squares2 = self.calc_diagonal(queen, for_king=True)
            threatened_squares.update(squares1)
            threatened_squares.update(squares2)

        return threatened_squares

    def calc_diagonal(self, piece, for_king=False):
        # UP AND LEFT
        row = piece.pos[0] + 1
        col = piece.pos[1] + 1
        while row < 8 and col < 8 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row += 1
            col += 1
        if row < 8 and col < 8 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # UP AND RIGHT
        row = piece.pos[0] + 1
        col = piece.pos[1] - 1
        while row < 8 and col >= 0 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row += 1
            col -= 1
        if row < 8 and col >= 0 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # DOWN AND LEFT
        row = piece.pos[0] - 1
        col = piece.pos[1] + 1
        while row >= 0 and col < 8 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row -= 1
            col += 1
        if row >= 0 and col < 8 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # DOWN AND RIGHT
        row = piece.pos[0] - 1
        col = piece.pos[1] - 1
        while row >= 0 and col >= 0 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row -= 1
            col -= 1
        if row >= 0 and col >= 0 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # Calculates if the opposing king would be in check after the move
        if for_king:
            return [move[-2:] for move in piece.legal_moves]

    def calc_cardinal(self, piece, for_king=False):
        # UP
        row = piece.pos[0] + 1
        col = piece.pos[1]
        while row < 8 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row += 1
        if row < 8 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # DOWN
        row = piece.pos[0] - 1
        col = piece.pos[1]
        while row >= 0 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            row -= 1
        if row >= 0 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # LEFT
        row = piece.pos[0]
        col = piece.pos[1] - 1
        while col >= 0 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            col -= 1
        if col >= 0 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # RIGHT
        row = piece.pos[0]
        col = piece.pos[1] + 1
        while col < 8 and isinstance(self.board[row][col], EmptySquare):
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)
            col += 1
        if col < 8 and self.board[row][col].colour != piece.colour:
            coords_converted = (self.col_dict_rev[col], str(row + 1))
            move_converted = piece.algebraic + 'x' + ''.join(coords_converted)
            piece.legal_moves.append(move_converted)

        # Calculates if the opposing king would be in check after the move
        if for_king:
            return [move[-2:] for move in piece.legal_moves]

    def calc_pawn(self, piece, for_king=False):
        potential_moves = []
        basic_move = (1, 0) if piece.colour == 1 else (-1, 0)  # Black moves down the board, white moves up
        starting_move = (2, 0) if piece.colour == 1 else (-2, 0)

        potential_moves.append(basic_move)

        if (piece.colour == 0 and piece.pos[0] == 6) or (piece.colour == 1 and piece.pos[0] == 1):
            potential_moves.append(starting_move)

        square_front = [piece.pos[0] + 1, piece.pos[1]] if piece.colour == 1 else [piece.pos[0] - 1, piece.pos[1]]

        # CHECKING IF NORMAL MOVES ARE LEGAL
        for potential_move in potential_moves:
            pos_after_move = (piece.pos[0] + potential_move[0], piece.pos[1])
            if isinstance(self.board[square_front[0]][square_front[1]], EmptySquare) and ((7 >= square_front[0]) >= 0) and (7 >= square_front[1] >= 0):
                coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                move_converted = ''.join(coords_converted)
                piece.legal_moves.append(move_converted)

        # CHECKING IF CAPTURES ARE LEGAL
        captures = [(1, 1) if piece.colour == 1 else (-1, 1), (1, -1) if piece.colour == 1 else (-1, -1)]
        possible_captures_notation = [] #For storing possible capture squares, used in checking for king checks.
        for capture in captures:
            pos_after_move = (piece.pos[0] + capture[0], piece.pos[1] + capture[1])
            if ((7 >= pos_after_move[0]) >= 0) and (7 >= pos_after_move[1] >= 0):
                coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                move_converted = self.col_dict_rev[piece.pos[1]] + 'x' + ''.join(coords_converted)
                possible_captures_notation.append(move_converted)
                if not (isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare)) and self.board[pos_after_move[0]][pos_after_move[1]].colour != piece.colour:
                    piece.legal_moves.append(move_converted)
                    piece.legal_captures.append(move_converted)

        # Calculates if the opposing king would be in check after the move
        if for_king:
            return [move[2:] for move in possible_captures_notation]

    def calc_knight(self, piece, for_king=False):
        potential_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for potential_move in potential_moves:
            pos_after_move = (piece.pos[0] + potential_move[0], piece.pos[1] + potential_move[1])
            if (7 >= pos_after_move[0] >= 0) and (7 >= pos_after_move[1] >= 0):
                if isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare):
                    coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                    move_converted = 'N' + ''.join(coords_converted)
                    piece.legal_moves.append(move_converted)
                elif self.board[pos_after_move[0]][pos_after_move[1]].colour != piece.colour:
                    coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                    move_converted = 'N' + 'x' + ''.join(coords_converted)
                    piece.legal_moves.append(move_converted)

        # Calculates if the opposing king would be in check after the move
        if for_king:
            return [move[-2:] for move in piece.legal_moves]



    def calc_king(self, piece, for_king=False):
        #FINDING SQUARES ATTACKED BY OPPOSING COLOUR:
        #TODO: IN CASES WHERE KING IS IN CHECK,
        #TODO: MOVES SHOULD BE LIMITED TO KING MOVES, MOVES THAT CAPTURE THE ATTACKER AND MOVES THAT DISRUPT THE ATTACKER

        threatened_squares = self.calc_threats(piece.colour)

        potential_moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

        for potential_move in potential_moves:
            pos_after_move = (piece.pos[0] + potential_move[0], piece.pos[1] + potential_move[1])
            if (7 >= pos_after_move[0] >= 0) and (7 >= pos_after_move[1] >= 0):
                if isinstance(self.board[pos_after_move[0]][pos_after_move[1]], EmptySquare):
                    coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                    move_converted = 'K' + ''.join(coords_converted)
                    if move_converted[-2:] not in threatened_squares:
                        piece.legal_moves.append(move_converted)
                elif self.board[pos_after_move[0]][pos_after_move[1]].colour != piece.colour:
                    coords_converted = (self.col_dict_rev[pos_after_move[1]], str((pos_after_move[0]) + 1))
                    move_converted = 'K' + 'x' + ''.join(coords_converted)
                    if move_converted[-2:] not in threatened_squares:
                        piece.legal_moves.append(move_converted)


        if for_king: #TODO: CHECK FOR OPPOSING KING MOVES AS WELL
            pass
    def legal_move(self, move, colour):
        piece_to_move = None
        legal = False
        check = False

        checking_dict = self.white_pieces if colour == 1 else self.black_pieces

        #PAWN
        if move[0] not in 'NBRQK':
            for pawn in checking_dict['P']: #Check every pawn
                self.calc_pawn(pawn)

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

                    potential_checker = pawn

                    self.board[last_row][last_col] = EmptySquare()

                pawn.legal_moves = []  # Reset legal moves

            if legal:
                self.calc_pawn(potential_checker)

                opposing_dict = self.black_pieces if potential_checker.colour == 1 else self.white_pieces
                king = opposing_dict['K'][0]
                algebraic_pos = (self.col_dict_rev[king.pos[1]] + str(king.pos[0] + 1))

                for move in potential_checker.legal_captures:
                    if move[2:] == algebraic_pos:
                        check = True

                potential_checker.legal_moves = []

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

                    potential_checker = rook

                    self.board[last_row][last_col] = EmptySquare()

                rook.legal_moves = []  # Reset legal moves

            if legal:
                self.calc_cardinal(potential_checker)

                opposing_dict = self.black_pieces if potential_checker.colour == 1 else self.white_pieces
                king = opposing_dict['K'][0]
                algebraic_pos = (self.col_dict_rev[king.pos[1]] + str(king.pos[0] + 1))

                for move in potential_checker.legal_moves:
                    if move[-2:] == algebraic_pos:
                        check = True

        #KNIGHT
        elif move[0] == 'N':
            for knight in checking_dict['N']:
                self.calc_knight(knight)


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

                    potential_checker = knight

                    self.board[last_row][last_col] = EmptySquare()

                knight.legal_moves = []  # Reset legal moves


            if legal:
                self.calc_knight(potential_checker)

                opposing_dict = self.black_pieces if potential_checker.colour == 1 else self.white_pieces
                king = opposing_dict['K'][0]
                algebraic_pos = (self.col_dict_rev[king.pos[1]] + str(king.pos[0] + 1))

                for move in potential_checker.legal_moves:
                    if move[-2:] == algebraic_pos:
                        check = True


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

                        potential_checker = bishop

                        self.board[last_row][last_col] = EmptySquare()

                    bishop.legal_moves = []  # Reset legal moves

            if legal:
                self.calc_diagonal(potential_checker)

                opposing_dict = self.black_pieces if potential_checker.colour == 1 else self.white_pieces
                king = opposing_dict['K'][0]
                algebraic_pos = (self.col_dict_rev[king.pos[1]] + str(king.pos[0] + 1))

                for move in potential_checker.legal_moves:
                    if move[-2:] == algebraic_pos:
                        check = True

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

                    potential_checker = queen

                    self.board[last_row][last_col] = EmptySquare()

                queen.legal_moves = []  # Reset legal moves

            if legal:
                self.calc_cardinal(potential_checker)
                self.calc_diagonal(potential_checker)

                opposing_dict = self.black_pieces if potential_checker.colour == 1 else self.white_pieces
                king = opposing_dict['K'][0]
                algebraic_pos = (self.col_dict_rev[king.pos[1]] + str(king.pos[0] + 1))

                for move in potential_checker.legal_moves:
                    if move[-2:] == algebraic_pos:
                        check = True


        #KING
        elif move[0] == 'K' or move == '0-0' or move == '0-0-0':
            #TODO: Implement castling moves

            for king in checking_dict['K']: #There will only ever be one king, but let's stay consistent with the rest of the program
                self.calc_king(king)


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

                        king.has_moved = True

                        self.board[last_row][last_col] = EmptySquare()

                    king.legal_moves = []  # Reset legal moves

        return legal, check