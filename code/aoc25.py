def read_input():
    with open("inputs/aoc_input_25.txt") as f:
        return int(f.readline().rstrip()), int(f.readline().rstrip())

def find_encryption_key(card_pk, door_pk):
    card_loop_size = find_loop_size(card_pk)
    door_loop_size = find_loop_size(door_pk)

    result = 1
    for i in range(door_loop_size):
        result *= card_pk
        result %= 20201227
    return result

def find_loop_size(pk):
    loop_size = 0
    result = 1
    while result != pk:
        loop_size += 1
        result *= 7
        result %= 20201227
    return loop_size

card_pk, door_pk = read_input()
print("Part 1: " + str(find_encryption_key(card_pk, door_pk)))
print("Part 2: Done! :)")