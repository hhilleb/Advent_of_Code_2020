from itertools import cycle

def read_input():
    with open("inputs/aoc_input_23.txt") as f:
        return [int(number) for number in f.readline().rstrip()]


def simulate_moves(cups_list, amount):
    # Fill dict and find cup with maximum label
    cups = {}
    max_label = 0
    for i in range(len(cups_list) - 1):
        if cups_list[i] > max_label:
            max_label = cups_list[i]
        cups[cups_list[i]] = cups_list[i+1]

    if cups_list[-1] > max_label:
        max_label = cups_list[-1]
    cups[cups_list[-1]] = cups_list[0]

    # Simulate game
    move = 0
    current_cup = cups_list[0]
    while move < amount:
        # Remove the next 3 cups
        next_cup = cups[cups[cups[cups[current_cup]]]]
        picked_up = list(reversed([cups.pop(cups[cups[current_cup]]), cups.pop(cups[current_cup]), cups.pop(current_cup)]))
        cups[current_cup] = next_cup

        # Find destination
        for i in range(1, 5):
            if current_cup - i <= 0:
                if max_label - i + current_cup not in picked_up:
                    destination = max_label - i + current_cup
                    break
            elif current_cup - i not in picked_up:
                destination = current_cup - i
                break

        # Place picked up cups at destination
        next_cup = cups[destination]
        cups[destination] = picked_up[0]
        cups[picked_up[0]] = picked_up[1]
        cups[picked_up[1]] = picked_up[2]
        cups[picked_up[2]] = next_cup

        # Set new current_cup
        current_cup = cups[current_cup]

        move += 1
    return cups


def get_cup_labels_after_one(cups):
    s = ""
    cup = 1
    for i in range(len(cups)-1):
        cup = cups[cup]
        s += str(cup)
    return s


def find_stars(cups):
    return cups[1] * cups[cups[1]]


cups = read_input()
print("Part 1: " + str(get_cup_labels_after_one(simulate_moves(cups, 100))))
print("Part 2: " + str(find_stars(simulate_moves(cups + [i for i in range(len(cups)+1, 1000001)], 10000000))))