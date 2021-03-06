import part_2

test_cases = [{
    'input': '2 * 3 + (4 * 5)',
    'expected_expr_tree': [
        2,
        '*',
        3,
        '+',
        [
            4,
            '*',
            5,
        ]
    ],
    'expected_result': 46,
},{
    'input': '5 + (8 * 3 + 9 + 3 * 4 * 3)',
    'expected_expr_tree': [
        5,
        '+',
        [
            8,
            '*',
            3,
            '+',
            9,
            '+',
            3,
            '*',
            4,
            '*',
            3,
        ]
    ],
    'expected_result': 1445,
},{
    'input': '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
    'expected_expr_tree': [
        5,
        '*',
        9,
        '*',
        [
            7,
            '*',
            3,
            '*',
            3,
            '+',
            9,
            '*',
            3,
            '+',
            [
                8,
                '+',
                6,
                '*',
                4,
            ]
        ]
    ],
    'expected_result': 669060,
},{
    'input': '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
    'expected_expr_tree': [
        [
            [
                2,
                '+',
                4,
                '*',
                9,
            ],
            '*',
            [
                6,
                '+',
                9,
                '*',
                8,
                '+',
                6,
            ],
            '+',
            6,
        ],
        '+',
        2,
        '+',
        4,
        '*',
        2,
    ],
    'expected_result': 23340,
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    expr_tree = part_2.parse_into_exp_tree(test_case['input'])
    assert_equals(expr_tree, test_case['expected_expr_tree'])

    result = part_2.compute(expr_tree)
    assert_equals(result, test_case['expected_result'])

print("")
print("[[[ SUCCESS ]]]")
print("")
