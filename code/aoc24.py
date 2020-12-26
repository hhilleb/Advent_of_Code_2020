def read_input():
    tiles = []
    with open("inputs/aoc_input_24.txt") as f:
        for line in f:
            tile = []
            while line != "\n" and line != "":
                if line[0] == 'e' or line[0] == 'w':
                    tile.append(line[0])
                    line = line[1:]
                else:
                    tile.append(line[0] + line[1])
                    line = line[2:]
            tiles.append(tile)
    return tiles


def flip_tiles(tiles):
    grid = {}   # coordinate -> how often flipped
    for tile in tiles:
        coord = [0,0]
        for dir in tile:
            if dir == 'e':
                coord[0] += 1
            elif dir == 'w':
                coord[0] -= 1
            elif dir == 'se':
                coord[1] += 1
            elif dir == 'sw':
                coord[0] -= 1
                coord[1] += 1
            elif dir == 'nw':
                coord[1] -= 1
            elif dir == 'ne':
                coord[0] += 1
                coord[1] -= 1
        if grid.get(tuple(coord)) == None:
            grid[tuple(coord)] = 1
        else:
            grid[tuple(coord)] += 1
    return grid

def count_black_tiles(grid):
    count = 0
    for tile in grid.values():
        if tile % 2 == 1:
            count += 1
    return count
    

def simulate_art(grid, days):
    for i in range(days):
        new_grid = grid.copy()
        for tile in grid.keys():
            if should_be_flipped(grid, tile):
                new_grid[tile] += 1

            neighbours = [(tile[0]+1, tile[1]), (tile[0]-1, tile[1]), (tile[0], tile[1]+1),
                        (tile[0]-1, tile[1]+1), (tile[0], tile[1]-1), (tile[0]+1, tile[1]-1)]
            for neighbour in neighbours:
                if grid.get(neighbour) == None and should_be_flipped(grid, neighbour):
                    new_grid[neighbour] = 1
        grid = new_grid
    return grid

def should_be_flipped(grid, tile):
    neighbours = [(tile[0]+1, tile[1]), (tile[0]-1, tile[1]), (tile[0], tile[1]+1),
                  (tile[0]-1, tile[1]+1), (tile[0], tile[1]-1), (tile[0]+1, tile[1]-1)]
    count = 0
    for neighbour in neighbours:
        if grid.get(neighbour) != None and grid[neighbour] % 2 == 1:
            count += 1
    if grid.get(tile) != None and grid[tile] % 2 == 1 and (count == 0 or count > 2):
        return True
    elif (grid.get(tile) == None or grid[tile] % 2 == 0) and count == 2:
        return True
    return False


grid = flip_tiles(read_input())
print("Part 1: " + str(count_black_tiles(grid)))
print("Part 2: " + str(count_black_tiles(simulate_art(grid,100))))