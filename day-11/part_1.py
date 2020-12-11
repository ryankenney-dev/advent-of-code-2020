
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
            if seat_empty_and_no_adjacent_occupied(seats, row, seat):
                changes[(row,seat)] = '#'
            elif seat_occupied_and_four_or_more_adjacent_occupied(seats, row, seat):
                changes[(row,seat)] = 'L'
    for change in changes.items():
        seats[change[0][0]][change[0][1]] = change[1]
    return len(changes)

def seat_empty_and_no_adjacent_occupied(seats, row, seat):
    if seats[row][seat] != 'L':
        return False
    adjacent_seats = get_adjacent_seats(seats, row, seat)
    return all(list(map(lambda s: seats[s[0]][s[1]] == 'L', adjacent_seats)))

def seat_occupied_and_four_or_more_adjacent_occupied(seats, row, seat):
    if seats[row][seat] != '#':
        return False
    adjacent_seats = get_adjacent_seats(seats, row, seat)
    occpied_count = sum(list(map(lambda s: map_occupied_to_int(seats, s[0], s[1]), adjacent_seats)))
    return occpied_count >= 4

def map_occupied_to_int(seats, row, seat):
    if seats[row][seat] == '#':
        return 1
    else:
        return 0

def get_adjacent_seats(seats, row, seat):
    adjacent_candidates = [
        (row-1,seat-1),(row-1,seat),(row-1,seat+1),
        (row,seat-1),(row,seat+1),
        (row+1,seat-1),(row+1,seat),(row+1,seat+1)
    ]
    adjacent_seats = []
    for adjacent_seat in adjacent_candidates:
        if adjacent_seat[0] < 0 or adjacent_seat[0] >= len(seats):
            continue
        elif adjacent_seat[1] < 0 or adjacent_seat[1] >= len(seats[adjacent_seat[0]]):
            continue
        elif seats[adjacent_seat[0]][adjacent_seat[1]] == '.':
            continue
        adjacent_seats.append(adjacent_seat)
    return adjacent_seats

