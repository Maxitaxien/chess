'''A place to store unused code (in case it is ever needed)'''


def show_board(self, colour=1):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if colour == 1:
        row_counter = 8
        for row in reversed(self.board):
            print(' '.join([str(piece) for piece in row]), row_counter)
            row_counter -= 1
    else:
        row_counter = 1
        for row in self.board:
            print(' '.join([str(piece) for piece in row]), row_counter)
            row_counter += 1
    print('  '.join([char for char in columns]))