import part_2

test_cases = [{
    'input': '''departure class: 0-1 or 4-19
row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9''',
    'expected_ticket_data': {
        'rules': {
            'departure class': [(0, 1), (4, 19)],
            'row': [(0, 5), (8, 19)],
            'departure seat': [(0, 13), (16, 19)] },
        'my_ticket': [11, 12, 13],
        'nearby_tickets':
            [[3,9,18], [15,1,5], [5,14,9]]},
    'expected_field_to_rule_map': ['row', 'departure class', 'departure seat'],
    'expected_product_departure_fields': 12*13
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))


for test_case in test_cases:
    ticket_data = part_2.parse_message(test_case['input'])
    print(ticket_data)
    assert_equals(ticket_data, test_case['expected_ticket_data'])
    field_to_rule_map = part_2.identify_field_to_rule_mapping(ticket_data)
    print(field_to_rule_map)
    assert_equals(field_to_rule_map, test_case['expected_field_to_rule_map'])
    product_departure_fields = part_2.compute_product_departure_fields(ticket_data)
    assert_equals(product_departure_fields, test_case['expected_product_departure_fields'])

print("")
print("[[[ SUCCESS ]]]")
print("")
