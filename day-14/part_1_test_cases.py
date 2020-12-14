import part_1

test_cases = [{
    'input': '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0''',
    'expected_sum': 165
}]

for test_case in test_cases:
    instructions = part_1.parse_to_instructions(test_case['input'])
    memory = part_1.execute_instructions(instructions)
    sum = part_1.sum_of_memory(memory)
    if sum != test_case['expected_sum']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_sum'], sum))

print("")
print("[[[ SUCCESS ]]]")
print("")
