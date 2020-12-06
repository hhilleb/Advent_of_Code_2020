import string

# PART 1
def sum_of_anyone():
    count = 0
    yes_answers = set()
    with open("inputs/aoc_input_6.txt") as f:
        for line in f:
            if line != "\n":
                for char in line.rstrip():
                    if char not in yes_answers:
                        yes_answers.add(char)
            else:
                count += len(yes_answers)
                yes_answers.clear()

    return count

# PART 2
def sum_of_everyone():
    count = 0
    common_answers = set(string.ascii_lowercase)
    with open("inputs/aoc_input_6.txt") as f:
        for line in f:
            if line != "\n":
                common_answers.intersection_update(line.rstrip())
            else:
                count += len(common_answers)
                common_answers = set(string.ascii_lowercase)

    return count

print("Part 1: " + str(sum_of_anyone()))
print("Part 2: " + str(sum_of_everyone()))