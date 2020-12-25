import part_1
import copy

test_cases = [{
    'input': '''5764801
17807724''',
    'exepected_loop_size': [
        8,
        11,
    ],
    'exepected_encryption_key': 14897079,
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    public_keys = part_1.parse_input(test_case['input'])
    loop_sizes = []
    for public_key, exepected_loop_size in zip(public_keys, test_case['exepected_loop_size']):
        loop_size = part_1.find_loop_size(7, public_key)
        loop_sizes.append(loop_size)
        assert_equals(loop_size, exepected_loop_size)
    for loop_size, public_key in zip(reversed(loop_sizes), public_keys):
        encryption_key = part_1.transform_subject_number(public_key, loop_size)
        assert_equals(encryption_key, test_case['exepected_encryption_key'])

    encryption_key = part_1.find_encryption_key(public_keys, 7)
    assert_equals(encryption_key, test_case['exepected_encryption_key'])

print("")
print("[[[ SUCCESS ]]]")
print("")
