import part_1

test_cases = [{
    'input': '''0,3,6''',
    'expected_sum': 436
}]

for test_case in test_cases:
    numbers = part_1.parse_to_numbers(test_case['input'])
    sum = part_1.compute_until_2020(numbers)
    if sum != test_case['expected_sum']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_sum'], sum))

print("")
print("[[[ SUCCESS ]]]")
print("")
