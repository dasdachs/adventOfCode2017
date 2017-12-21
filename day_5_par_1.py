input = [int(x) for x in input.splitlines()]

def move(array):
   ...:     pos = 0
   ...:     moves = 0
   ...:     while pos < len(array):
   ...:         next_move = array[pos]
   ...:
   ...:         array[pos] += 1
   ...:         pos += next_move
   ...:         moves += 1
   ...:     return moves
