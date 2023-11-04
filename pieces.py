class Pawn:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
    def capture(self):
        pass

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
        self.legal_moves = []

    def __str__(self):
        return 'N_' + self.colour

class Bishop:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []

    def show_legal_moves(self):
        pass

    def __str__(self):
        return 'B_' + self.colour
class Rook:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []


    def __str__(self):
        return 'R_' + self.colour
class Queen:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []

    def __str__(self):
        return 'Q_' + self.colour
class King:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
        self.in_check = False
        self.legal_moves = []
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
        return ' _ '
