import part_1

test_cases = [
    { 'input': 'BFFFBBFRRR', 'expected_row': 70, 'expected_column': 7, 'expected_seat_id': 567 },
    { 'input': 'FFFBBBFRRR', 'expected_row': 14, 'expected_column': 7, 'expected_seat_id': 119 },
    { 'input': 'BBFFBBFRLL', 'expected_row': 102, 'expected_column': 4, 'expected_seat_id': 820 }
]

for test_case in test_cases:
    row = part_1.get_row(test_case['input'][0:8])
    if test_case['expected_row'] != row:
        raise Exception('Expected row %s, but saw %s' % (test_case['expected_row'], row))
    col = part_1.get_col(test_case['input'][7:])
    if test_case['expected_column'] != col:
        raise Exception('Expected column %s, but saw %s' % (test_case['expected_column'], col))
    seat_id = part_1.get_seat_id(test_case['input'])
    if test_case['expected_seat_id'] != seat_id:
        raise Exception('Expected seat_id %s, but saw %s' % (test_case['expected_seat_id'], seat_id))

print("")
print("[[[ SUCCESS ]]]")
print("")
