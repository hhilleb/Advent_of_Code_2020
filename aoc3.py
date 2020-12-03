trees = {}

with open('aoc_input_3.txt') as f:
    for row, line in enumerate(f):
        for col, char in enumerate(line):
            if char == '#':
                trees[col, row] = 1


def check_slopes(slopes):
    """Multiplies the number of tree collisions on each slope

    Args:
        slopes (list of tuples): each tuple represents a slope with the first tuple entry
        being the number of steps in the right direction and the second tuple entry being
        the number of steps downwards"""

    result = 1
    for slope in slopes:
        pos = (0,0)
        collisions = 0
        for i in range(row + 1):
            pos = ((pos[0] + slope[0]) % (col + 1), pos[1] + slope[1])
            if trees.get(pos) != None:
                collisions += 1
        result *= collisions
    return result

# PART 1
#slopes = [(3,1)]

#PART 2
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

print(check_slopes(slopes))