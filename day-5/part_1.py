
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
    return current_offset

def get_seat_id(location_code):
    row = get_row(location_code[0:8])
    col = get_col(location_code[7:])
    return row * 8 + col
