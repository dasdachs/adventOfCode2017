def shuffle(mem):
     ...:     # Find the biggest block by size and index
     ...:     # set the block to 0 and spread the value
     ...:     # over the whole memory
     ...:     biggest_block = sorted(mem, reverse=True)[0]
     ...:     start_index = mem.index(biggest_block)
     ...:     mem[start_index] = 0
     ...:
     ...:     while biggest_block > 0:
     ...:         start_index = (start_index + 1) % len(mem)
     ...:         mem[start_index] += 1
     ...:         biggest_block -= 1
     ...:     return mem
     
     def reallocation(mem):
     ...:     states = [mem]
     ...:     realocated = mem
     ...:     itteration = 0
     ...:     while True:
     ...:         if itteration % 1000 == 0:
     ...:             print(f"Itteration number {itteration}")
     ...:         realocated = shuffle(realocated)
     ...:         realocated_string = "".join([str(x) for x in realocated])
     ...:         itteration += 1
     ...:         if realocated_string in states:
                      diff = itteration - states.index(realocated_string)
     ...:             return itteration, diff # 1st is for part one, the 2nd for part two
     ...:         states.append(realocated_string)
