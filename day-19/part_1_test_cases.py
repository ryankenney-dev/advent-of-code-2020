import part_1
import re

test_cases = [{
    'input': '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb''',
    'expected_rules': {
        0: {'seq': [4, 1, 5]},
        1: {'or':[ {'seq':[2, 3]}, {'seq':[3, 2]}]},
        2: {'or':[ {'seq':[4, 4]}, {'seq':[5, 5]}]},
        3: {'or':[ {'seq':[4, 5]}, {'seq':[5, 4]}]},
        4: 'a',
        5: 'b',
    },
    'expected_messages': [
        'ababbb',
        'bababa',
        'abbbab',
        'aaabbb',
        'aaaabbb',
    ],
    'expected_regex': r'^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b$',
    'expected_test_all_result': [
        (True, 'ababbb'),
        (False, 'bababa'),
        (True, 'abbbab'),
        (False, 'aaabbb'),
        (False, 'aaaabbb'),
    ]
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    parsed = part_1.parse_input(test_case['input'])
    assert_equals(parsed['rules'], test_case['expected_rules'])
    assert_equals(parsed['messages'], test_case['expected_messages'])

    regex = part_1.to_regex(parsed['rules'])
    assert_equals(regex, test_case['expected_regex'])

    result = part_1.test_all_messages(test_case['input'])
    assert_equals(result, test_case['expected_test_all_result'])

print("")
print("[[[ SUCCESS ]]]")
print("")
