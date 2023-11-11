for knight in checking_dict['N']:
    potential_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

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