import re
import itertools

def count_matches(ver):
    unfinished = []     # [[rule number1, [option1, option2, ...]], ...]
    matches = {}        # rule number -> set of matches

    with open("inputs/aoc_input_19.txt") as f:
        # read rules
        line = f.readline().rstrip()
        while line != "":
            rule = re.split(": | \| ", line.rstrip())
            if rule[1] == '"a"':
                matches[rule[0]] = set('a')
            elif rule[1] == '"b"':
                matches[rule[0]] = set('b')
            else:
                options = [re.split(" ", option) for option in rule[1:]]
                unfinished.append([rule[0], options])

            line = f.readline().rstrip()
  
        # calculate set of matching strings for each rule
        matches = calculate_matches(unfinished, matches)

        # count number of input strings that match
        count = 0
        no_match = []
        for line in f:
            if line.rstrip() in matches['0']:
                count += 1
            else:
                no_match.append(line.rstrip())

        # there are potentially more input strings that match in part 2
        if ver == 2:
            for line in no_match:
                # Note that strings that match rule 42 or rule 31 have length 8
                if len(line) % 8 == 0:
                    parts = [line[0+i:i+8] for i in range(0, len(line), 8)]
                    
                    # The string has to match (42)^m (31)^n with 1 <= n < m
                    state = "check 42"
                    discard = False
                    count42 = 0
                    count31 = 0
                    for part in parts:
                        if state == "check 42":
                            if part in matches['42']:
                                count42 += 1
                            elif part in matches['31']:
                                state = "check 31"
                                count31 += 1
                            else:
                                discard = True
                        elif state == "check 31":
                            if part in matches['31']:
                                count31 += 1
                            else:
                                discard = True

                    if (not discard) and count42 >= 1 and count31 >= 1 and count42 > count31:
                        if line not in matches['0']:
                            count += 1
        return count


def calculate_matches(unfinished, matches):
    while unfinished != []:
        # Search for rule which can be constructed from known matches
        for rule in unfinished:
            unknown_rule = False
            for options in rule[1]:
                for rule_num in options:
                    if matches.get(rule_num) == None:
                        unknown_rule = True
                        break
            if not unknown_rule:
                # Apply matches for rule
                matches[rule[0]] = set()
                new_match = set()

                for option in rule[1]:
                    combinations = list(itertools.product(*[matches[i] for i in option]))
                    for i in combinations:
                        new_match.add("".join(i))
                    matches[rule[0]] = matches[rule[0]].union(new_match)
                unfinished.remove(rule)

    return matches

print("Part 1: " + str(count_matches(1)))
print("Part 2: " + str(count_matches(2)))