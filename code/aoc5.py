rows = 128
columns = 8

# PART 1
def find_max(rows, columns):
    cur_max = -1
    with open('inputs/aoc_input_5.txt') as f:
        for line in f:
            cur_front = 0
            cur_bottom = rows - 1
            cur_left = 0
            cur_right = columns - 1

            for char in line:
                if char == 'F':
                    cur_bottom = (cur_front + cur_bottom)//2
                elif char == 'B':
                    cur_front = ((cur_front + cur_bottom)//2) + 1
                elif char == 'L':
                    cur_right = (cur_left + cur_right)//2
                elif char == 'R':
                    cur_left = ((cur_left + cur_right)//2) + 1

            seat_id = cur_front * columns + cur_left
            if seat_id > cur_max:
                cur_max = seat_id

    return cur_max

# PART 2
def find_own_seat(rows, columns):
    seats = set()

    with open('inputs/aoc_input_5.txt') as f:
        cur_max = -1
        cur_min = rows*columns + 1
        for line in f:
            cur_front = 0
            cur_bottom = rows - 1
            cur_left = 0
            cur_right = columns - 1

            for char in line:
                if char == 'F':
                    cur_bottom = (cur_front + cur_bottom)//2
                elif char == 'B':
                    cur_front = ((cur_front + cur_bottom)//2) + 1
                elif char == 'L':
                    cur_right = (cur_left + cur_right)//2
                elif char == 'R':
                    cur_left = ((cur_left + cur_right)//2) + 1
            
            seat_id = cur_front * columns + cur_left
            seats.add(seat_id)
            if seat_id > cur_max:
                cur_max = seat_id
            if seat_id < cur_min:
                cur_min = seat_id

        for i in range(cur_min, cur_max + 1):
                if i not in seats and (i-1) in seats and (i+1) in seats:
                    return i

print("Part 1 " + str(find_max(rows, columns)))
print("Part 2: " + str(find_own_seat(rows, columns)))
