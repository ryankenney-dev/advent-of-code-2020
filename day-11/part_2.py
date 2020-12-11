
def parse_to_seats_array(message):
    lines = message.splitlines()
    result = []
    for line in lines:
        result.append(list(line))
    return result

def dump_seats_to_string(seats):
    rows = []
    for row in seats:
        rows.append(''.join(row))
    return '\n'.join(rows)

def process_until_stable_return_occupied_count(seats):
    while True:
        changes = process_one_round_and_return_change_count(seats)
        if changes == 0:
            break
    occupied_count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied_count = occupied_count + 1
    return occupied_count

def process_one_round_and_return_change_count(seats):
    changes = {}
    for row in range(0,len(seats)):
        for seat in range(0,len(seats[row])):
            if seat_empty_and_no_visible_occupied(seats, (row, seat)):
                changes[(row,seat)] = '#'
            elif seat_occupied_and_five_or_more_visible_occupied(seats, (row, seat)):
                changes[(row,seat)] = 'L'
    for change in changes.items():
        seats[change[0][0]][change[0][1]] = change[1]
    return len(changes)

def seat_empty_and_no_visible_occupied(seats, seat):
    if seats[seat[0]][seat[1]] != 'L':
        return False
    all_visible_occupied = not any(list(map( \
        lambda i: seat_in_direction_is_visibly_occupied(seats, seat, i), \
        get_cardinal_incrementors())))
    return all_visible_occupied

def seat_occupied_and_five_or_more_visible_occupied(seats, seat):
    if seats[seat[0]][seat[1]] != '#':
        return False
    occupied_count = sum(list(map( \
        lambda i: seat_in_direction_is_visibly_occupied(seats, seat, i), \
        get_cardinal_incrementors())))
    return occupied_count >= 5

def map_occupied_to_int(seats, row, seat):
    if seats[row][seat] == '#':
        return 1
    else:
        return 0

def get_cardinal_incrementors():
    return [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1)
    ]

def seat_in_direction_is_visibly_occupied(seats, seat, incrementor):
    next_seat = (seat[0] + incrementor[0], seat[1] + incrementor[1])
    while seat_inbounds(seats, next_seat):
        seat_char = seats[next_seat[0]][next_seat[1]]
        if seat_char == '#':
            return True
        if seat_char == 'L':
            return False
        next_seat = (next_seat[0] + incrementor[0], next_seat[1] + incrementor[1])
    return False

def seat_inbounds(seats, seat):
    if seat[0] < 0 or seat[0] >= len(seats):
        return False
    if seat[1] < 0 or seat[1] >= len(seats[seat[0]]):
        return False
    return True
