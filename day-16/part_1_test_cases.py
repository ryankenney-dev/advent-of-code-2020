import part_1

test_cases = [{
    'input': '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12''',
    'expected_ticket_data': {
        'rules': [
            {'name': 'class', 'ranges': [(1, 3), (5, 7)]},
            {'name': 'row', 'ranges': [(6, 11), (33, 44)]},
            {'name': 'seat', 'ranges': [(13, 40), (45, 50)]}],
        'nearby_tickets':
            [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]},
    'expected_invalid_field_values': [4, 55, 12],
    'expected_sum_invalid_field_values': 71
}]

for test_case in test_cases:
    ticket_data = part_1.parse_message(test_case['input'])
    print(ticket_data)
    if ticket_data != test_case['expected_ticket_data']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_ticket_data'], ticket_data))
    invalid_field_values = part_1.find_invalid_nearby_ticket_field_values(ticket_data)
    if invalid_field_values != test_case['expected_invalid_field_values']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_invalid_field_values'], invalid_field_values))
    sum_invalid_field_values = sum(part_1.find_invalid_nearby_ticket_field_values(ticket_data))
    if sum_invalid_field_values != test_case['expected_sum_invalid_field_values']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_sum_invalid_field_values'], sum_invalid_field_values))

print("")
print("[[[ SUCCESS ]]]")
print("")
