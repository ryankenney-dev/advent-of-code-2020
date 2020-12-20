import part_2
import re

test_cases = [{
    'input': '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31 | 42 11 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42 | 42 8
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba''',
    'expected_test_all_result': [
        (False, 'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa'),
        (True, 'bbabbbbaabaabba'),
        (True, 'babbbbaabbbbbabbbbbbaabaaabaaa'),
        (True, 'aaabbbbbbaaaabaababaabababbabaaabbababababaaa'),
        (True, 'bbbbbbbaaaabbbbaaabbabaaa'),
        (True, 'bbbababbbbaaaaaaaabbababaaababaabab'),
        (True, 'ababaaaaaabaaab'),
        (True, 'ababaaaaabbbaba'),
        (True, 'baabbaaaabbaaaababbaababb'),
        (True, 'abbbbabbbbaaaababbbbbbaaaababb'),
        (True, 'aaaaabbaabaaaaababaa'),
        (False, 'aaaabbaaaabbaaa'),
        (True, 'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa'),
        (False, 'babaaabbbaaabaababbaabababaaab'),
        (True, 'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'),
    ]
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    parsed = part_2.parse_input(test_case['input'])
    result = part_2.test_all_messages(test_case['input'])
    assert_equals(result, test_case['expected_test_all_result'])

print("")
print("[[[ SUCCESS ]]]")
print("")
