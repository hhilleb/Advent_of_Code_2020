import re
import math

class Tile:
    def __init__(self, tile_id, layout):
        self.tile_id = tile_id
        self.layout = layout
        self.options = self.get_options()

    def rotate_right(self):
        self.layout = list((zip(*self.layout[::-1])))

    def flip_horizontal(self):
        new_layout = []
        for row in self.layout:
            new_layout.append(tuple(reversed(row)))
        self.layout = new_layout

    def flip_vertical(self):
        new_layout = []
        for row in self.layout:
            new_layout.insert(0, row)
        self.layout = new_layout

    def get_options(self):
        options = set()
        for i in range(4):
            options.add(tuple(self.layout))

            self.flip_vertical()
            options.add(tuple(self.layout))
            self.flip_vertical()

            self.flip_horizontal()
            options.add(tuple(self.layout))
            self.flip_horizontal()

            self.rotate_right()
        return options

    def __str__(self):
        s = ""
        for row in self.layout:
            s = s + "".join(row) + "\n"
        return s


def read_input():
    tiles = []
    with open("inputs/aoc_input_20.txt") as f:
        for line in f:
            if "Tile" in line:
                tile_id = int(re.split(" |:", line)[1])
                layout = []
            elif line == "\n":
                tiles.append(Tile(tile_id, layout))
            else:
                layout.append(tuple(line.rstrip()))
    return tiles

def find_corners(tiles):
    # corners only have 2 common edges with other tiles
    count = {}
    for tile in tiles:
        count[tile] = 0

    for tile1 in tiles:
        for tile2 in tiles:
            if tile1 != tile2:
                if have_common_edges(tile1, tile2):
                    count[tile1] += 1

    mul = 1
    for tile, n in zip(count.keys(), count.values()):
        if n == 2:
            mul = mul * tile.tile_id
    return mul

def have_common_edges(tile1, tile2):
    edges1 = set()
    edges2 = set()

    for option in tile1.get_options():
        edges1.add(option[0])
        edges1.add(option[-1])
        edges1.add(tuple([row[0] for row in option]))
        edges1.add(tuple([row[-1] for row in option]))
    
    for option in tile2.get_options():
        edges2.add(option[0])
        edges2.add(option[-1])
        edges2.add(tuple([row[0] for row in option]))
        edges2.add(tuple([row[-1] for row in option]))

    for edge in edges1:
        if edge in edges2:
            return True
    return False

tiles = read_input()
print("Part 1: " + str(find_corners(tiles)))






######### My pitiful attempts at reconstructing the image for part 1... ###########


# image = [None for i in range(len(tiles))]
   

# def solve(image, free_tiles):
#     if image[-1] != None:
#         return image
#     else:
#         for pos in range(len(image)):
#             if image[pos] == None:
#                 # Check any compatible tile
#                 for tile in free_tiles:
#                     compatible_tiles = get_compatible_tiles(image, pos, tile)
#                     for compatible_tile in compatible_tiles:
#                         image[pos] = compatible_tile
#                         free_tiles.remove(tile)
#                         result = solve(image, free_tiles)
#                         if result == None:
#                             image[pos] = None
#                             free_tiles.add(tile)
#                 return None


# def get_compatible_tiles(image, pos, tile):
#     if pos == 0:
#         return tile.options.copy()
#     else:
#         compatible_tiles = tile.options.copy()
#         for option in tile.options.copy():
#             if pos in range(int(math.sqrt(len(image)))):
#                 # check left
#                 if not is_compatible(option, image[pos-1], 'left'):
#                     compatible_tiles.remove(option)
#             elif (pos-1) % math.sqrt(len(image)) == 0:
#                 # check oben
#                 if not is_compatible(option, image[pos - int(math.sqrt(len(image)))], 'top'):
#                     compatible_tiles.remove(option)
#             else:
#                 # check oben
#                 if not is_compatible(option, image[pos - int(math.sqrt(len(image)))], 'top'):
#                     compatible_tiles.remove(option)
#                 # check left
#                 elif not is_compatible(option, image[pos-1], 'left'):
#                     compatible_tiles.remove(option)
#         return compatible_tiles

# def is_compatible(tile1, tile2, dir):
#     if tile2 == None:
#         return True
#     elif dir == 'top':
#         return tile1[0] == tile2[-1]
#     elif dir == 'left':
#         return [row[0] for row in tile1] == [row[-1] for row in tile2]

# print(solve(image, set(tiles)))