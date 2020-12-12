# PART 1
def calculate_manhattan_distance_1():
    dir = 90        # 0 = north, 90 = east, 180 = south, 270 = west
    pos = [0, 0]    # [east, north]

    with open("inputs/aoc_input_12.txt") as f:
        for line in f:
            instr = line[0]
            num = int(line[1:])
            
            if instr == 'L':
                dir = (dir - num) % 360
            elif instr == 'R':
                dir = (dir + num) % 360
            elif instr == 'F':
                move(dir, num, pos)
            elif instr == 'N':
                move(0, num, pos)
            elif instr == 'E':
                move(90, num, pos)
            elif instr == 'S':
                move(180, num, pos)
            elif instr == 'W':
                move(270, num, pos)
    return abs(pos[0]) + abs(pos[1])

def move(dir, num, pos):
    if dir == 0:
        pos[1] += num
    elif dir == 90:
        pos[0] += num
    elif dir == 180:
        pos[1] -= num
    elif dir == 270:
        pos[0] -= num


# PART 2
def calculate_manhattan_distance_2():
    pos = [0, 0]              # [east, north]
    waypoint_pos = [10, 1]    # [east, north]

    with open("inputs/aoc_input_12.txt") as f:
        for line in f:
            instr = line[0]
            num = int(line[1:])
            if instr == 'R':
                for i in range(int((num / 90) % 4)):
                    waypoint_pos = [waypoint_pos[1], waypoint_pos[0] * -1]
            elif instr == 'L':
                for i in range(int((num / 90) % 4)):
                    waypoint_pos = [waypoint_pos[1] * -1, waypoint_pos[0]]
            elif instr == 'F':
                move(90, num * waypoint_pos[0], pos)
                move(0, num * waypoint_pos[1], pos)
            elif instr == 'N':
                move(0, num, waypoint_pos)
            elif instr == 'E':
                move(90, num, waypoint_pos)
            elif instr == 'S':
                move(180, num, waypoint_pos)
            elif instr == 'W':
                move(270, num, waypoint_pos)
    return abs(pos[0]) + abs(pos[1])

print("Part 1: " + str(calculate_manhattan_distance_1()))
print("Part 2: " + str(calculate_manhattan_distance_2()))