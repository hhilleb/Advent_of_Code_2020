import math
from functools import reduce

with open("inputs/aoc_input_13.txt") as f:
    earliest_departure = int(f.readline())
    # buses[i] = (pos of i in input, bus id of i)
    buses = [(bus[0], int(bus[1])) for bus in enumerate(f.readline().rstrip().split(",")) if bus[1] != 'x']


# PART 1
def waiting_time_times_bus_id(earliest_departure, buses):
    earliest_bus = [-1, float('inf')]   # [bus id, departure time]

    for bus in buses:
        earliest_possible = bus[1] * math.ceil(earliest_departure/bus[1])
        if earliest_possible < earliest_bus[1]:
            earliest_bus = [bus[1], earliest_possible]

    waiting_time = earliest_bus[1] - earliest_departure
    return earliest_bus[0] * waiting_time


# PART 2
def win_contest(buses):
    n = [bus[1] for bus in buses]
    a = [-bus[0] for bus in buses]
    return chinese_remainder(n, a)

# Chinese remainder theorem from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print("Part 1: " + str(waiting_time_times_bus_id(earliest_departure, buses)))
print("Part 2: " + str(win_contest(buses)))