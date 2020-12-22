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
    'expected_winning_score': 291
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    hands = part_2.parse_input(test_case['input'])
    assert_equals(hands, test_case['expected_parsed_hands'])
    hands = copy.deepcopy(test_case['expected_parsed_hands'])
    winning_hand_id = part_2.play_whole_game(hands)
    winning_score = part_2.compute_score(hands[winning_hand_id])
    assert_equals(winning_score, test_case['expected_winning_score'])

print("")
print("[[[ SUCCESS ]]]")
print("")
