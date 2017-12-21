def move(array):
    ...:     pos = 0
    ...:     moves = 0
    ...:     while pos < len(array):
    ...:         next_move = array[pos]
    ...:
    ...:         if next_move >= 3:
    ...:             array[pos] -= 1
    ...:         else:
    ...:             array[pos] += 1
    ...:
    ...:         pos += next_move
    ...:         moves += 1
    ...:     return moves
