import part_2
import json

test_cases = [{
    'input': '389125467',
    'expected_rounds': {
        0: [2, 8, 9, 1, 5, 4, 6, 7, 3],
        1: [5, 4, 6, 7, 8, 9, 1, 3, 2],
        2: [8, 9, 1, 3, 4, 6, 7, 2, 5],
        3: [4, 6, 7, 9, 1, 3, 2, 5, 8],
        4: [1, 3, 6, 7, 9, 2, 5, 8, 4],
        5: [9, 3, 6, 7, 2, 5, 8, 4, 1],
        6: [2, 5, 8, 3, 6, 7, 4, 1, 9],
        7: [6, 7, 4, 1, 5, 8, 3, 9, 2],
        8: [5, 7, 4, 1, 8, 3, 9, 2, 6],
        9: [8, 3, 7, 4, 1, 9, 2, 6, 5],
    },
    'expectd_product_after_10': 18,
    'expectd_product_after_10m': 149245887792
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    game = part_2.Game(test_case['input'], 9)
    for i in range(0, 10):
        print(game.to_label_list())
        game.run_cycle()
        if i not in test_case['expected_rounds']:
            continue
        assert_equals( \
            game.to_label_list(), \
            test_case['expected_rounds'][i])
    product = game.set_product_of_two_labels_after_1()
    assert_equals(product, test_case['expectd_product_after_10'])

    game = part_2.Game(test_case['input'], 1000000)
    for i in range(0, 10000000):
        game.run_cycle()
    product = game.set_product_of_two_labels_after_1()
    assert_equals(product, test_case['expectd_product_after_10m'])

print("")
print("[[[ SUCCESS ]]]")
print("")
