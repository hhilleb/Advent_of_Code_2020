import re

memory = {}

def execute(ver):
    with open("inputs/aoc_input_14.txt") as f:
        for line in f:
            instr = re.split(" = |\[|\] = ", line.rstrip())
            if instr[0] == 'mask':
                mask = instr[1]
            elif instr[0] == 'mem':
                if ver == 1:
                    memory[instr[1]] = int(mask_binary(mask, bin(int(instr[2]))[2:].zfill(36), 1),2)
                if ver == 2:
                    address = list(mask_binary(mask, bin(int(instr[1]))[2:].zfill(36), 2))
                    flaoting_pos = [i for i, bit in enumerate(address) if bit == 'X']
                    for i in range(2**len(flaoting_pos)):
                        new_bits = list(bin(i)[2:].zfill(len(flaoting_pos)))
                        for j in range(len(flaoting_pos)):
                            address[flaoting_pos[j]] = new_bits[j]
                        memory[int("".join(address),2)] = int(instr[2])

def mask_binary(mask, num, ver):
    result = ""
    if ver == 1:
        for mask_bit, num_bit in zip(mask, num):
            if mask_bit != 'X':
                result += mask_bit
            else:
                result += num_bit
    elif ver == 2:
        for mask_bit, num_bit in zip(mask, num):
            if mask_bit == '0':
                result += num_bit
            else:
                result += mask_bit
    return result


def sum_of_memory(ver):
    execute(ver)
    return sum(memory.values())

print("Part 1: " + str(sum_of_memory(1)))
memory = {}
print("Part 2: " + str(sum_of_memory(2)))