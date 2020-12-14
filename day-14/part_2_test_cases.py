import part_2

test_cases = [{
    'input': '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1''',
    'expected_sum': 208
}]

for test_case in test_cases:
    instructions = part_2.parse_to_instructions(test_case['input'])
    memory = part_2.execute_instructions(instructions)
    sum = part_2.sum_of_memory(memory)
    if sum != test_case['expected_sum']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_sum'], sum))

print("")
print("[[[ SUCCESS ]]]")
print("")
