# PART 1
def find_invalid_number():
    # Calculates each sum only one time (longer code but less math :))
    numbers = [] # the 25 relevant numbers
    sums = []    # list of lists; list i contains numbers[i+1] + numbers[0:i+1]
    with open("inputs/aoc_input_9.txt") as f:
        i = 0
        for line in f:
            num = int(line.rstrip())
            if i >= 25 and not is_sum(sums, num):
                return num
            numbers, sums = add_element(numbers, sums, num)
            i += 1
    return None

def add_element(numbers, sums, new):
    numbers.append(new)
    if len(numbers) <= 25:
        if len(numbers) != 1:
            new_sums = []
            for num in numbers:
                if new != num:
                    new_sums.append(num + new)
            sums.append(new_sums)
    else:
        numbers.pop(0)
        # Delete first element of each list, add new list for new sums
        sums.pop(0)
        for i in sums:
            i.pop(0)
        new_sums = []
        for num in numbers:
            if new != num:
                new_sums.append(num + new)
        sums.append(new_sums)
    return numbers, sums

def is_sum(sums, num):
    for i in sums:
        if num in i:
            return True
    return False


# PART 2
def calculate_encryption_weakness(invalid_number):
    with open("inputs/aoc_input_9.txt") as f:
        numbers = [int(line.rstrip()) for line in f]
    
    for i in range(len(numbers)):
        sum = 0
        j = 0
        interval = []
        while sum < invalid_number:
            interval.append(numbers[i + j])
            sum += numbers[i + j]
            j += 1
        if sum == invalid_number:
            return min(interval) + max(interval)
    return None

print("Part 1: " + str(find_invalid_number()))
print("Part 2: " + str((calculate_encryption_weakness(find_invalid_number()))))