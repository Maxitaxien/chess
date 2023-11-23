class Pawn:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
    def promote(self, move):
        pass
    def __str__(self):
        return 'P_' + ('W' if self.colour == 1 else 'B')


class Knight:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.next_moves = [] #Used for checking possible captures after movement, to see if king is put in check

    def __str__(self):
        return 'N_' + ('W' if self.colour == 1 else 'B')

class Bishop:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []

    def __str__(self):
        return 'B_' + ('W' if self.colour == 1 else 'B')
class Rook:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []

    def __str__(self):
        return 'R_' + ('W' if self.colour == 1 else 'B')
class Queen:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []

    def __str__(self):
        return 'Q_' + ('W' if self.colour == 1 else 'B')
class King:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
        self.in_check = False
        self.legal_moves = []

    def __str__(self):
        return 'K_' + ('W' if self.colour == 1 else 'B')

class EmptySquare:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def __str__(self):
        return ' _ '
