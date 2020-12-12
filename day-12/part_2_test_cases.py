import part_2

test_cases = [{
    'input': '''F10
N3
F7
R90
F11''',
    'expected_manhattan_distance': 286
}]

for test_case in test_cases:
    instructions = part_2.parse_message_to_instructions(test_case['input'])
    distance = part_2.process_instructions_to_manhattan_distance(instructions)
    if distance != test_case['expected_manhattan_distance']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_manhattan_distance'], distance))

print("")
print("[[[ SUCCESS ]]]")
print("")
