with open('inputs/aoc_input_1.txt') as f:
    numbers = [int(line.rstrip()) for line in f]

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x + y + z == 2020:
                print(x*y*z)
                exit()

print("Nothing found...")
