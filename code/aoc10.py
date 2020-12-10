with open("inputs/aoc_input_10.txt") as f:
    adapters = [int(line.rstrip()) for line in f]

def calculate_differences(given_adapters):
    adapters = given_adapters.copy()
    adapters.sort()

    diffs = {1:0, 2:0, 3:0}
    joltage = 0

    for adapter in adapters:
        diff = adapter - joltage
        joltage += diff
        diffs[diff] += 1
    return diffs[1] * (diffs[3] + 1)

def calculate_combinations(given_adapters):
    adapters = given_adapters.copy()
    adapters.sort()

    # the i'th position tells how many combinations there are to reach a joltage of i
    combination_count = [1,]
    if 1 in adapters:
        combination_count.append(1)
        if 2 in adapters:
            combination_count.append(2)
        else:
            combination_count.append(0)
    else:
        combination_count.append(0)
        if 2 in adapters:
            combination_count.append(1)
        else:
            combination_count.append(0)
    
    for i in range(3,adapters[-1]+1):
        if i in adapters:
            combination_count.append(combination_count[i-1] + combination_count[i-2] + combination_count[i-3])
        else:
            combination_count.append(0)
            
    return combination_count[-1]


print("Part 1: " + str(calculate_differences(adapters)))
print("Part 2: " + str(calculate_combinations(adapters)))
