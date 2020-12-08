with open("inputs/aoc_input_8.txt") as f:
    boot_code = [line.rstrip() for line in f]

def execute(boot_code):
    """Runs provided boot code and returns the result. Stops on infinite loop

    Args:
        boot_code (list of string): List of instructions representing boot code

    Returns:
        (bool, int): bool is True if the code terminates and False otherwise
                     int gives the final value of the accumulator or its value before the infinite loop
    """
    ic = 0
    acc = 0
    executed_lines = set()
    while ic < len(boot_code):
        instruction = boot_code[ic].split(" ")
        if ic not in executed_lines:
            executed_lines.add(ic)        # Mark line as executed
            if instruction[0] == "acc":
                acc += int(instruction[1])
                ic += 1
            elif instruction[0] == 'jmp':
                ic += int(instruction[1])
            else:
                ic += 1
        else:
            return (False, acc)
    return (True, acc)

def fix_code(boot_code):
    result = (False, 1)
    for i in range(len(boot_code)):
        instruction = boot_code[i].split(" ")
        if instruction[0] == "jmp":
            boot_code[i] = "nop " + instruction[1]
            result = execute(boot_code)
            boot_code[i] = "jmp " + instruction[1]
        elif instruction[0] == "nop":
            boot_code[i] = "jmp " + instruction[1]
            result = execute(boot_code)
            boot_code[i] = "nop " + instruction[1]

        if result[0] == True:
            print(i)
            return result[1]

    return None

print("Part 1: " + str(execute(boot_code)[1]))
print("Part 2: " + str(fix_code(boot_code)))