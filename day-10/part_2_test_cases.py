import part_2

test_cases = [{
    'input': '''16
10
15
5
1
11
7
19
6
12
4''',
    'expected_to_include': [
        [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22],
        [0, 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, 22],
        [0, 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, 22],
        [0, 1, 4, 5, 7, 10, 12, 15, 16, 19, 22],
        [0, 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, 22],
        [0, 1, 4, 6, 7, 10, 12, 15, 16, 19, 22],
        [0, 1, 4, 7, 10, 11, 12, 15, 16, 19, 22],
        [0, 1, 4, 7, 10, 12, 15, 16, 19, 22],
    ],
    'expected_combinations': 8
},{
    'input': '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3''',
    'expected_to_include': [
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52],
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, 52],
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, 52],
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 49, 52],
        [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, 52],
        [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 46, 48, 49, 52],
        [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 46, 49, 52],
        [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 47, 48, 49, 52],
        [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 47, 49, 52],
        [0, 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 48, 49, 52],
    ],
    'expected_combinations': 19208

}]

for test_case in test_cases:
    jolt_adapters = part_2.parse_jolt_adapters(test_case['input'])
    combinations = part_2.find_all_combinations(jolt_adapters)
    for expected_combo in test_case['expected_to_include']:
        if expected_combo not in combinations:
            raise Exception('Missing combo: %s' % expected_combo)
    if len(combinations) != test_case['expected_combinations']:
        raise Exception('Unexpected')
    combinations_count = part_2.count_all_combinations(jolt_adapters)
    if combinations_count != test_case['expected_combinations']:
        raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
