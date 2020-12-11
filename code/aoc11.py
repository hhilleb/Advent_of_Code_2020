import copy

grid = []

with open("inputs/aoc_input_11.txt") as f:
    # Create the grid with a border of '-' to avoid edge cases
    t = f.tell()
    length = len(f.readline())
    f.seek(t)
    grid.append(['-' for i in range(length+1)])
    for line in f:
        stripped = line.rstrip()
        grid.append(['-'] + [char for char in stripped] + ['-'])
    grid.append(['-' for i in range(length+1)])


def simulate(grid, part):
    changed = True
    while changed:
        grid, changed = do_round(grid, part)
    return grid

def do_round(grid, part):
    change = False
    new_grid = copy.deepcopy(grid)
    if part == 1:
        tolerance = 4
    elif part == 2:
        tolerance = 5

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] != '.':
                occupied = sees_how_many_occupied_seats(grid, i, j, part)
                if occupied == 0 and grid[i][j] == 'L':
                    new_grid[i][j] = '#'
                    change = True
                elif occupied >= tolerance and grid[i][j] == '#':
                    new_grid[i][j] = 'L'
                    change = True

    return (new_grid, change)

def sees_how_many_occupied_seats(grid, i, j, part):
    if part == 1:
        return [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                grid[i][j-1],                 grid[i][j+1],
                grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]].count('#')
    elif part == 2:
        sees = []
        for dir in ['l','r','u','d','ul','ur','dl','dr']:
            x = j
            y = i
            deltaX = 0
            deltaY = 0
            if 'l' in dir:
                deltaX = -1
            elif 'r' in dir:
                deltaX = 1
            if 'u' in dir:
                deltaY = 1
            elif 'd' in dir:
                deltaY = -1
            while grid[y + deltaY][x + deltaX] == '.':
                x += deltaX
                y += deltaY
            sees.append(grid[y + deltaY][x + deltaX])
        return sees.count('#')

def count_occupied_seats(grid):
    sum = 0
    for i in grid:
        sum += i.count('#')
    return sum


print("Part 1: " + str(count_occupied_seats(simulate(grid, 1))))
print("Part 2: " + str(count_occupied_seats(simulate(grid, 2))))