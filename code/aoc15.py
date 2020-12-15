def calculate_ith_number(i):
    numbers = {}    # number -> list of turns in which the number was spoken

    with open("inputs/aoc_input_15.txt") as f:
        for t, num in enumerate(f.readline().rstrip().split(',')):
            numbers[int(num)] = [t + 1,]

    last_said = int(num)

    for turn in range(t + 2, i + 1):
        if len(numbers[last_said]) == 1:
            numbers[0].append(turn)
            last_said = 0
        else:
            age = numbers[last_said][-1] - numbers[last_said][-2]
            if numbers.get(age) == None:
                numbers[age] = [turn,]
            else:
                numbers[age].append(turn)
            last_said = age
    return last_said

print("Part 1: " + str(calculate_ith_number(2020)))
print("Part 1: " + str(calculate_ith_number(30000000)))