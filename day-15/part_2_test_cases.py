import part_2

test_cases = [{
    'input': '''0,3,6''',
    'expected_result': 175594
},{
    'input': '''1,3,2''',
    'expected_result': 2578
},{
    'input': '''2,1,3''',
    'expected_result': 3544142
},{
    'input': '''1,2,3''',
    'expected_result': 261214
},{
    'input': '''2,3,1''',
    'expected_result': 6895259
},{
    'input': '''3,2,1''',
    'expected_result': 18
},{
    'input': '''3,1,2''',
    'expected_result': 362
}]

for test_case in test_cases:
    numbers = part_2.parse_to_numbers(test_case['input'])
    result = part_2.compute_until(numbers, 30000000)
    if result != test_case['expected_result']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_result'], result))

print("")
print("[[[ SUCCESS ]]]")
print("")
