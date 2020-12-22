import part_2
import copy

test_cases = [{
    'input': '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10''',
    'expected_parsed_hands': [
        [9, 2, 6, 3, 1],
        [5, 8, 4, 7, 10]
    ],
    'expected_rounds': {
        2: ([2, 6, 3, 1, 9, 5], [8, 4, 7, 10]),
        3: ([6, 3, 1, 9, 5], [4, 7, 10, 8, 2]),
        4: ([3, 1, 9, 5, 6, 4], [7, 10, 8, 2]),
        5: ([1, 9, 5, 6, 4], [10, 8, 2, 7, 3]),
        27: ([5, 4, 1], [8, 9, 7, 3, 2, 10, 6]),
        28: ([4, 1], [9, 7, 3, 2, 10, 6, 8, 5]),
        29: ([1], [7, 3, 2, 10, 6, 8, 5, 9, 4]),
    },
    'expected_winning_score': 306
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    hands = part_2.parse_input(test_case['input'])
    assert_equals(hands, test_case['expected_parsed_hands'])
    round = 1
    while len(hands[0]) > 1 and len(hands[1]) > 1:
        round += 1
        part_2.play_round(hands[0], hands[1])
        if round in test_case['expected_rounds']:
            assert_equals(hands[0], test_case['expected_rounds'][round][0])
            assert_equals(hands[1], test_case['expected_rounds'][round][1])
    hands = copy.deepcopy(test_case['expected_parsed_hands'])
    winning_score = part_2.play_whole_game(hands[0], hands[1])
    assert_equals(winning_score, test_case['expected_winning_score'])

print("")
print("[[[ SUCCESS ]]]")
print("")
