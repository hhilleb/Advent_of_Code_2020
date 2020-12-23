import re
import math

class Tile:
    def __init__(self, tile_id, layout):
        self.tile_id = tile_id
        self.layout = layout
        self.options = self.get_options()
        self.neighbours = {}

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

    def add_common_edges(self, tile2):
        edges1 = set()
        edges2 = set()

        for option in self.options:
            edges1.add(option[0])
            edges1.add(option[-1])
            edges1.add(tuple([row[0] for row in option]))
            edges1.add(tuple([row[-1] for row in option]))
        
        for option in tile2.options:
            edges2.add(option[0])
            edges2.add(option[-1])
            edges2.add(tuple([row[0] for row in option]))
            edges2.add(tuple([row[-1] for row in option]))

        for edge in edges1:
            if edge in edges2:
                self.neighbours[edge] = tile2
                self.neighbours[tuple(reversed(edge))] = tile2

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


def construct_image(tiles):
    # Find common edges for all tiles
    for tile1 in tiles:
        for tile2 in tiles:
            if tile1 != tile2:
                tile1.add_common_edges(tile2)

    # Create empty image
    size = int(math.sqrt(len(tiles)))
    image = [[None for i in range(size)] for j in range(size)]

    # Find a corner tile
    for tile in tiles:
        if len(tile.neighbours.values()) == 4:
            image[0][0] = tile
            break

    # Rotate/flip corner tile correctly
    for option in image[0][0].options:
        bottom_edge = option[-1]
        right_edge = tuple([row[-1] for row in option])
        if image[0][0].neighbours.get(bottom_edge) != None and image[0][0].neighbours.get(right_edge) != None:
            image[0][0].layout = option
            break

    # Complete top row
    for i in range(1, size):
        left_tile = image[0][i-1]
        connecting_edge = tuple([row[-1] for row in left_tile.layout])
        new_tile = left_tile.neighbours[connecting_edge]

        image[0][i] = new_tile

        # Rotate new tile correctly
        for option in image[0][i].options:
            left_edge = tuple([row[0] for row in option])
            if left_edge == connecting_edge:
                image[0][i].layout = option
                break
    
    # Complete the rest of the image
    for row in range(1, size):
        # Place leftmost tile of row
        top_tile = image[row-1][0]
        connecting_edge = top_tile.layout[-1]
        new_tile = top_tile.neighbours[connecting_edge]

        image[row][0] = new_tile

        # Rotate new tile correctly
        for option in image[row][0].options:
            top_edge = option[0]
            left_edge = tuple([row[0] for row in option])
            if top_edge == connecting_edge and image[row][0].neighbours.get(left_edge) == None:
                image[row][0].layout = option
                break

        # Complete the rest of the row
        for col in range(1,size):
            top_tile = image[row-1][col]
            connecting_edge_top = top_tile.layout[-1]

            left_tile = image[row][col-1]
            connecting_edge_left = tuple([row[-1] for row in left_tile.layout])

            new_tile = top_tile.neighbours[connecting_edge_top]

            image[row][col] = new_tile

            # Rotate new tile correctly
            for option in image[row][col].options:
                top_edge = option[0]
                left_edge = tuple([row[0] for row in option])
                if top_edge == connecting_edge_top and left_edge == connecting_edge_left:
                    image[row][col].layout = option
                    break

    return image


def multiply_corners(image):
    return image[0][0].tile_id * image[0][-1].tile_id * image[-1][0].tile_id * image[-1][-1].tile_id

def search_for_seamonsters(image):
    # Convert image to tile (to remove borders and to rotate/flip it easily)
    image = convert_image(image)
    correctly_rotated = False
    for layout in image.options:
        layout = list(layout)
        seamonster_mask = [(1,0),(2,1),(2,4),(1,5),(1,6),(2,7),(2,10),(1,11),(1,12),(2,13),(2,16),(1,17),(0,18),(1,18),(1,19)]
        
        for r in range(len(layout)-2):
            for c in range(len(layout)-19):
                # Check for seamonster at this position
                found_seamonster = True
                for coord in seamonster_mask:
                    if layout[r+coord[0]][c+coord[1]] != '#':
                        found_seamonster = False
                if found_seamonster:
                    correctly_rotated = True
                    # Mark seamonster
                    for coord in seamonster_mask:
                        new_row = list(layout[r+coord[0]])
                        new_row[c+coord[1]] = 'O'
                        layout[r+coord[0]] = tuple(new_row)
        if correctly_rotated:
            break

    # Find the number of # that are not part of a seamonster
    count = 0
    for row in layout:
        count += row.count('#')
    return(count)

def convert_image(image):
    # remove borders
    for row_image in range(len(image)):
        for col_image in range(len(image)):
            tile = image[row_image][col_image]
            tile.layout = list(tile.layout[1:-1])
            for i in range(len(tile.layout)):
                tile.layout[i] = tuple(list(tile.layout[i])[1:-1])

    layout = []
    for row_image in range(len(image)):
        for row_tile in range(len(image[0][0].layout)):
            row = []
            for col_image in range(len(image)):
                row.extend(image[row_image][col_image].layout[row_tile])
            layout.append(tuple(row))
    return Tile(None, layout)


def print_image(image):
    s = ""
    for row_image in range(len(image)):
        for row_tile in range(len(image[0][0].layout)):
            for col_image in range(len(image)):
                s += "".join(image[row_image][col_image].layout[row_tile])
                s += "  "
            s += "\n"
        s += "\n"
    print(s)


image = construct_image(read_input())
print("Part 1: " + str(multiply_corners(image)))
print("Part 2: " + str(search_for_seamonsters(image)))