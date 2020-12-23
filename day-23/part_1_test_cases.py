import part_1
import copy

test_cases = [{
    'input': '389125467',
    'expected_rounds': [
        [2, 8, 9, 1, 5, 4, 6, 7, 3],
        [5, 4, 6, 7, 8, 9, 1, 3, 2],
        [8, 9, 1, 3, 4, 6, 7, 2, 5],
        [4, 6, 7, 9, 1, 3, 2, 5, 8],
        [1, 3, 6, 7, 9, 2, 5, 8, 4],
        [9, 3, 6, 7, 2, 5, 8, 4, 1],
        [2, 5, 8, 3, 6, 7, 4, 1, 9],
        [6, 7, 4, 1, 5, 8, 3, 9, 2],
        [5, 7, 4, 1, 8, 3, 9, 2, 6],
        [8, 3, 7, 4, 1, 9, 2, 6, 5],
    ],
    'expected_signaures': {
        0: '54673289',
        1: '32546789',
        2: '34672589',
        3: '32584679',
        9: '92658374',
        99: '67384529',
    }
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    cups = part_1.parse_input(test_case['input'])
    for expected_cups in test_case['expected_rounds']:
        cups = part_1.run_cycle(cups)
        assert_equals(cups, expected_cups)

    cups = part_1.parse_input(test_case['input'])
    for i in range(0, 105):
        cups = part_1.run_cycle(cups)
        if i in test_case['expected_signaures']:
            assert_equals(part_1.get_cycle_signature(cups),
                test_case['expected_signaures'][i])

print("")
print("[[[ SUCCESS ]]]")
print("")
