import part_1

test_cases = [{
    'input': '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL''',
    'expected_rounds': ['''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##''',
        '''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##''',
        '''#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##''',
        '''#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##''',
        '''#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##'''
    ],
    'expected_occupied_when_stable': 37
}]

for test_case in test_cases:
    seats = part_1.parse_to_seats_array(test_case['input'])
    round_i = 0
    for expected_round in test_case['expected_rounds']:
        round_i = round_i + 1
        part_1.process_one_round_and_return_change_count(seats)
        seats_str = part_1.dump_seats_to_string(seats)
        if seats_str != expected_round:
            raise Exception('Round %s\nExpected:\n%s\nActual:\n%s' % (round_i, expected_round, seats_str))
    seats = part_1.parse_to_seats_array(test_case['input'])
    occupied_count = part_1.process_until_stable_return_occupied_count(seats)
    if occupied_count != test_case['expected_occupied_when_stable']:
        raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
