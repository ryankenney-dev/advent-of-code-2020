import part_2

test_cases = [{
    'input': '''xxx
7,13,x,x,59,x,31,19''',
    'expected_timestamp': 1068781
},{
    'input': '''xxx
17,x,13,19''',
    'expected_timestamp': 3417
},{
    'input': '''xxx
67,7,59,61''',
    'expected_timestamp': 754018
},{
    'input': '''xxx
67,x,7,59,61''',
    'expected_timestamp': 779210
},{
    'input': '''xxx
67,7,x,59,61''',
    'expected_timestamp': 1261476
},{
    'input': '''xxx
1789,37,47,1889''',
    'expected_timestamp': 1202161486
}]

for test_case in test_cases:
    buses = part_2.parse_to_buses_sorted_by_interval(test_case['input'])
    print(buses)
    timestamp = part_2.find_time_with_bus_offsets(buses)

    # TODO: Remove debug
    # print('%s %s %s' % (test_case['expected_timestamp'], timestamp, timestamp /test_case['expected_timestamp']))

    if timestamp != test_case['expected_timestamp']:
        raise Exception('Expected %s but saw %s' % (test_case['expected_timestamp'], timestamp))

print("")
print("[[[ SUCCESS ]]]")
print("")
