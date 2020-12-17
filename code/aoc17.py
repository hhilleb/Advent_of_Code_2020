def boot(dim):
    if dim == 3:
        dimension = {}  # (x,y,z) -> '#' or None
        with open("inputs/aoc_input_17.txt") as f:
            for row, line in enumerate(f):
                for col, char in enumerate(line.rstrip()):
                    if char == '#':
                        dimension[col, row, 0] = '#'
        
    elif dim == 4:
        dimension = {}  # (x,y,z,w) -> '#' or None
        with open("inputs/aoc_input_17.txt") as f:
            for row, line in enumerate(f):
                for col, char in enumerate(line.rstrip()):
                    if char == '#':
                        dimension[col, row, 0, 0] = '#'

    for i in range(6):
        dimension = do_cycle(dimension, dim)

    return len(dimension)


def do_cycle(dimension, dim):
    new_dimension = {}
    for coord in dimension.keys():
        neighbours = count_neighbours(coord, dimension, dim)
        # check if cube remains active
        if neighbours == 2 or neighbours == 3:
            new_dimension[coord] = '#'
        # check if any inactive neighbour becomes active
        if dim == 3:
            x, y, z = coord
            for a in [x-1, x, x+1]:
                for b in [y-1, y, y+1]:
                    for c in [z-1, z, z+1]:
                        if (a!=x or b!=y or c!=z) and count_neighbours((a,b,c), dimension, 3) == 3:
                            new_dimension[(a,b,c)] = '#'
        elif dim == 4:
            x, y, z, w = coord
            for a in [x-1, x, x+1]:
                for b in [y-1, y, y+1]:
                    for c in [z-1, z, z+1]:
                        for d in [w-1, w, w+1]:
                            if (a!=x or b!=y or c!=z or d != w) and count_neighbours((a,b,c,d), dimension, 4) == 3:
                                new_dimension[(a,b,c,d)] = '#'
    return new_dimension
        

def count_neighbours(coord, dimension, dim):
    sum = 0
    if dim == 3:
        x, y, z = coord
        for a in [x-1, x, x+1]:
            for b in [y-1, y, y+1]:
                for c in [z-1, z, z+1]:
                    if (a!=x or b!=y or c!=z) and dimension.get((a,b,c))=='#':
                        sum += 1
    if dim == 4:
        x, y, z, w = coord
        for a in [x-1, x, x+1]:
            for b in [y-1, y, y+1]:
                for c in [z-1, z, z+1]:
                    for d in [w-1, w, w+1]:
                        if (a!=x or b!=y or c!=z or d!=w) and dimension.get((a,b,c,d))=='#':
                            sum += 1
    return sum


print("Part 1: " + str(boot(3)))
print("Part 2: " + str(boot(4)))