import re

req_fields = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
target = len(req_fields)

valid_passports = 0
valid_fields = 0
fields_found = set()

with open("aoc_input_4.txt") as f:
    for line in f:
        if line != "\n":
            # PART 1
            #valid_fields += len([True for attr in line.split(" ") if attr.split(":")[0] in req_fields])

            # PART 2
            for fields in line.split(" "):
                arg, val = fields.rstrip().split(":")

                if (arg not in fields_found and 
                    ((arg == "byr" and int(val) >= 1920 and int(val) <= 2002) or
                    (arg == "iyr" and int(val) >= 2010 and int(val) <= 2020) or
                    (arg == "eyr" and int(val) >= 2020 and int(val) <= 2030) or
                    (arg == "hgt" and ((val[-2:] == "cm" and int(val[:-2]) >= 150 and int(val[:-2]) <= 193) or
                                       (val[-2:] == "in" and int(val[:-2]) >= 59 and int(val[:-2]) <= 76))) or
                    (arg == "hcl" and re.search("^#[a-f0-9]{6}$", val)) or
                    (arg == "ecl" and re.search("amb|blu|brn|gry|grn|hzl|oth", val)) or
                    (arg == "pid" and re.search("^[0-9]{9}$", val)))):
                    valid_fields += 1
                    fields_found.add(arg)  
            # PART 2 END            
                    
        else:
            if valid_fields == target:
                valid_passports += 1
            valid_fields = 0
            fields_found.clear()

print(valid_passports)