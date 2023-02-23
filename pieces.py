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
        pass

class Pawn(Piece):
    def __init__(self):
        pass

    def show_legal_moves(self):
        movelist = [1,0]
        if not has_moved():
            movelist.append([2,0])

        #TODO: Make enemy_piece thing
        #if pos == enemy_pos:
            #take

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