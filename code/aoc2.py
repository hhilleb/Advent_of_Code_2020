import re

with open('inputs/aoc_input_2.txt') as f:
    lines = [re.split("-| |: ", line.rstrip()) for line in f]

n = 0

# PART 1
# for i in lines:
#     occ = i[3].count(i[2])
#     if occ >= int(i[0]) and occ <= int(i[1]):
#         n += 1

# PART 2
for i in lines:
    a = i[3][int(i[0])-1] == i[2]
    b = i[3][int(i[1])-1] == i[2]
    if bool(a) != bool(b): # xor
        n += 1

print(n)