import re
              
def read_input():
    rules = {}      # field name -> list of tuple of int, e.g. location -> [(35,796),(811,953)]

    with open("inputs/aoc_input_16.txt") as f:
        line = f.readline()
        while line != "\n":
            rule = re.split(": |-| or |\n", line)[:-1]
            rules[rule[0]] = []
            for i in range(1,len(rule),2):
                rules[rule[0]].append((int(rule[i]), int(rule[i+1])))
            line = f.readline()
        
        f.readline()
        my_ticket = f.readline().rstrip().split(',')
        f.readline()
        f.readline()

        tickets = []
        for line in f:
            tickets.append([int(num) for num in line.rstrip().split(',')])

    return rules, my_ticket, tickets

# PART 1
def discard_invalid_tickets(rules, tickets):
    error_rate = 0
    invalid_tickets = []
    for ticket in tickets:
        for num in ticket:
            satisfies_rule = False
            for rule in rules.values():
                for interval in rule:
                    if interval[0] <= num and num <= interval[1]:
                        satisfies_rule = True
            if not satisfies_rule:
                invalid_tickets.append(ticket)
                error_rate += num

    for invalid_ticket in invalid_tickets:
        tickets.remove(invalid_ticket)

    return error_rate


# PART 2
def deduce_fields(rules, my_ticket, tickets):
    # the ith position tells what the ith field could possibly be
    possible_fields = [[i,] + list(rules.keys()) for i in range(len(rules.keys()))]
    
    # determine possible fields for each position
    for ticket in tickets:
        for i, num in enumerate(ticket):
            for rule in zip(rules.keys(), rules.values()):
                satisfies_rule = False
                for interval in rule[1]:
                    if interval[0] <= num and num <= interval[1]:
                        satisfies_rule = True
                if satisfies_rule == False and rule[0] in possible_fields[i]:
                    possible_fields[i].remove(rule[0])

    # deduce the final position of each field (expects that it's unambiguous)
    possible_fields.sort(key = len)

    fields = {}
    while possible_fields != []:
        pos, field = possible_fields.pop(0)
        fields[field] = pos
        for i in possible_fields:
            if field in i:
                i.remove(field)

    # multiply required positions of my ticket
    result = 1
    for field, pos in zip(fields.keys(), fields.values()):
        if field[0:9] == "departure":
            result *= int(my_ticket[pos])

    return result


rules, my_ticket, tickets = read_input()
print("Part 1: " + str(discard_invalid_tickets(rules, tickets)))
print("Part 2: " + str(deduce_fields(rules, my_ticket, tickets)))