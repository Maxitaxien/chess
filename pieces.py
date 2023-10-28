class Pawn:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos
        self.has_moved = False
    def show_legal_moves(self):
        if self.colour == 'B':
            basic_move = [1, 0]
            starting_move = [2, 0]
            movelist = basic_move
            if not self.has_moved:
                movelist.append([2,0])

        elif self.colour == 'W':
            basic_move = [0, 1]
            starting_move = [0, 2]
            movelist = basic_move
            if not self.has_moved:
                movelist.append(starting_move)

        #TODO: Make capture rules
        #if pos == enemy_pos:
            #take = [1, -1], [-1, -1]

    def promote(selfs):
        pass

    def move(self):
        self.has_moved = True
        pass


class Knight:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

class Bishop:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass
class Rook:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass
class Queen:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

    def show_legal_moves(self):
        pass
class King:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos
        self.has_moved = False

    def show_legal_moves(self):
        pass

    def move(self):
        self.has_moved = True
        pass