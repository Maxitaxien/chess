class Pawn:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.legal_captures = []
        self.algebraic = 'P'
        self.has_moved = False
    def promote(self, move):
        pass
    def __str__(self):
        return '♙' if self.colour == 1 else '♟'


class Knight:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.algebraic = 'K'
        self.next_moves = [] #Used for checking possible captures after movement, to see if king is put in check
        self.has_moved = False

    def __str__(self):
        return '♘' if self.colour == 1 else '♞'

class Bishop:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.algebraic = 'B'
        self.has_moved = False

    def __str__(self):
        return '♗' if self.colour == 1 else '♝'
class Rook:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.algebraic = 'R'
        self.has_moved = False

    def __str__(self):
        return '♖' if self.colour == 1 else '♜'
class Queen:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.legal_moves = []
        self.algebraic = 'Q'
        self.has_moved = False

    def __str__(self):
        return '♕' if self.colour == 1 else '♛'
class King:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
        self.in_check = False
        self.legal_moves = []
        self.algebraic = 'K'

    def __str__(self):
        return '♔' if self.colour == 1 else '♚'

class EmptySquare:
    def __init__(self, colour=None, pos=None):
        self.colour = colour
        self.pos = pos

    def __str__(self):
        return ' '


