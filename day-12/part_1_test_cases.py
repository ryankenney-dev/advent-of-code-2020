import part_1

test_cases = [{
    'input': '''F10
N3
F7
R90
F11''',
    'expected_manhattan_distance': 25
}]

for test_case in test_cases:
    instructions = part_1.parse_message_to_instructions(test_case['input'])
    distance = part_1.process_instructions_to_manhattan_distance(instructions)
    if distance != test_case['expected_manhattan_distance']:
        raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
