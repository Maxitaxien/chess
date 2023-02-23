class Piece:
    def __init__(self, colour, pos):
        self.colour = colour
        self.pos = pos

    def legal_moves(self):
        pass

    def move(self):
        pass

    def has_moved(self):
        moved = False
        return moved

    def pos(self):
        #TODO: Make function that returns current piece position on board.

class Pawn(Piece):
    def __init__(self):
        super().__init__()

    def legal_moves(self):
        if self.colour == 'B':
            basic_move = [0, -1]
            starting_move = [0, -2]
            movelist = basic_move
            if not has_moved(): #TODO: Implement has_moved()
                movelist.append([2,0])
        elif self.colour == 'W':
            basic_move = [0, 1]
            starting_move = [0, 2]
            movelist = basic_move
            if not has_moved():  # TODO: Implement has_moved()
                movelist.append(starting_move)

        #TODO: Make enemy_piece thing
        #if pos == enemy_pos:
            #take = [1, -1], [-1, -1]

    def pos(self):
        pass

class Knight(Piece):
    def __init__(self):
        super().__init__(self, colour)
        moves = []

    def pos(self):
        pass

class Bishop(Piece):
    def __init__(self):
        super().__init__(self, colour)
        moves = []

    def pos(self):
        pass

class Rook(Piece):
    def __init__(self):
        super().__init__(self, colour)
        moves = []

    def pos(self):
        pass

class Queen(Piece):
    def __init__(self):
        super().__init__(self, colour)
        moves = []

    def pos(self):
        pass

class King(Piece):
    def __init__(self):
        super().__init__(self, colour)
        moves = []

    def pos(self):
        pass