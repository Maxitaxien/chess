class Pawn:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
        self.movelist = []
    def show_legal_moves(self):
        basic_move = (1, 0) if self.colour == 'B' else (-1, 0)
        starting_move = (2, 0) if self.colour == 'B' else [-2, 0]

        #TODO: Check legality of moves before appending

        self.movelist.append(basic_move)

        if not self.has_moved:
            self.movelist.append(starting_move)

        #MAKE CAPTURE RULES
        #if pos == enemy_pos:

    def promote(self):
        pass

    def move(self, coord):
        if coord in self.movelist:
            #MOVE
            self.has_moved = True
        pass

    def __str__(self):
        return 'P_' + self.colour


class Knight:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos


    def __str__(self):
        return 'N_' + self.colour

class Bishop:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass

    def __str__(self):
        return 'B_' + self.colour
class Rook:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass

    def __str__(self):
        return 'R_' + self.colour
class Queen:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass

    def __str__(self):
        return 'Q_' + self.colour
class King:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
        self.in_check = False
    def show_legal_moves(self):
        pass

    def move(self):
        self.has_moved = True
        pass

    def __str__(self):
        return 'K_' + self.colour


class EmptySquare:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def __str__(self):
        return ' W '