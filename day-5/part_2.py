
def get_row(location_code):
    return get_row_or_col(location_code, 128, 'B')

def get_col(location_code):
    return get_row_or_col(location_code, 8, 'R')

def get_row_or_col(location_code, initial_span, high_char):
    span_size = initial_span
    current_offset = 0
    for c in location_code:
        if c == high_char:
            current_offset = current_offset + span_size/2
        span_size = span_size / 2
    return int(current_offset)

def get_seat_id(location_code):
    row = get_row(location_code[0:8])
    col = get_col(location_code[7:])
    return row * 8 + col

def find_my_seat(location_codes):
    occupied_seats = [False] * 1024
    for location_code in location_codes:
        occupied_seats[get_seat_id(location_code)] = True
    current_occupied = None
    prev_1_occupied = None
    prev_2_occupied = None
    for i in range(0,len(occupied_seats)):
        current_occupied = occupied_seats[i]
        if current_occupied == True and prev_1_occupied == False and prev_2_occupied == True:
            print('FOUND: %s' % (i-1))
            #return prev_1
        prev_2_occupied = prev_1_occupied
        prev_1_occupied = current_occupied

