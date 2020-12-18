import part_1

test_cases = [{
    'input': '''.#.
..#
###''',
    'expected_parsed_cubes': {
        (1,0,0),
        (2,1,0),
        (0,2,0),
        (1,2,0),
        (2,2,0),
    },
    'expected_bounds': {
        'x': (0, 2),
        'y': (0, 2),
        'z': (0, 0),
    },
    'expected_grown_bounds': {
        'x': (-1, 3),
        'y': (-1, 3),
        'z': (-1, 1),
    },
    'expected_adjacent_active_1_1_1': 5,
    'exepcted_active_after_6_cycles': 112
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    parsed_cubes = part_1.parse_to_active_cubes(test_case['input'])
    assert_equals(parsed_cubes, test_case['expected_parsed_cubes'])

    bounds = part_1.find_bounds(parsed_cubes)
    assert_equals(bounds, test_case['expected_bounds'])

    grown_bounds = part_1.grow_bounds(bounds)
    assert_equals(grown_bounds, test_case['expected_grown_bounds'])

    adjacent_count = part_1.count_adjacent_active(parsed_cubes, (1,1,1))
    assert_equals(adjacent_count, test_case['expected_adjacent_active_1_1_1'])

    active_cubes = part_1.process_6_cycles(parsed_cubes)
    assert_equals(len(active_cubes), test_case['exepcted_active_after_6_cycles'])

print("")
print("[[[ SUCCESS ]]]")
print("")
