import part_1
import copy

test_cases = [{
    'input': '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew''',
    'exepected_tile_paths': [
        ['se', 'se', 'nw', 'ne', 'ne', 'ne', 'w', 'se', 'e', 'sw', 'w', 'sw', 'sw', 'w', 'ne', 'ne', 'w', 'se', 'w', 'sw'],
        ['ne', 'e', 'e', 'ne', 'se', 'nw', 'nw', 'w', 'sw', 'ne', 'ne', 'w', 'nw', 'w', 'se', 'w', 'ne', 'nw', 'se', 'sw', 'e', 'sw'],
        ['se', 'sw', 'ne', 'sw', 'sw', 'se', 'nw', 'w', 'nw', 'se'],
        ['nw', 'nw', 'ne', 'se', 'e', 'sw', 'sw', 'ne', 'ne', 'w', 'ne', 'sw', 'w', 'ne', 'w', 'se', 'sw', 'ne', 'se', 'e', 'ne'],
        ['sw', 'w', 'e', 'sw', 'ne', 'sw', 'ne', 'nw', 'se', 'w', 'nw', 'ne', 'ne', 'se', 'e', 'nw'],
        ['e', 'e', 'se', 'nw', 'se', 'sw', 'sw', 'ne', 'nw', 'sw', 'nw', 'nw', 'se', 'w', 'w', 'nw', 'se', 'ne'],
        ['se', 'w', 'ne', 'ne', 'ne', 'ne', 'se', 'nw', 'se', 'w', 'ne', 'nw', 'w', 'w', 'se'],
        ['w', 'e', 'nw', 'w', 'w', 'e', 'se', 'e', 'e', 'w', 'e', 'sw', 'w', 'w', 'nw', 'w', 'e'],
        ['w', 'sw', 'e', 'e', 'se', 'ne', 'ne', 'w', 'nw', 'w', 'nw', 'se', 'ne', 'w', 'se', 'nw', 'w', 'se', 'se', 'se', 'nw', 'ne'],
        ['ne', 'e', 'sw', 'se', 'e', 'nw', 'w', 'sw', 'nw', 'sw', 'sw', 'nw'],
        ['ne', 'nw', 'sw', 'w', 'se', 'w', 'sw', 'ne', 'ne', 'ne', 'w', 'se', 'nw', 'se', 'nw', 'ne', 'se', 'se', 'ne', 'w'],
        ['e', 'ne', 'w', 'nw', 'e', 'w', 'ne', 'sw', 'se', 'w', 'nw', 'sw', 'e', 'nw', 'e', 'sw', 'ne', 'nw', 'se', 'nw', 'sw'], 
        ['sw', 'e', 'ne', 'sw', 'ne', 'sw', 'ne', 'ne', 'e', 'nw', 'ne', 'w', 'e', 'ne', 'w', 'w', 'ne', 'sw', 'sw', 'ne', 'se'],
        ['sw', 'w', 'e', 'se', 'ne', 'se', 'w', 'e', 'nw', 'ne', 'sw', 'nw', 'w', 'ne', 'se', 'sw', 'w', 'ne'],
        ['e', 'ne', 'se', 'nw', 'sw', 'w', 'sw', 'ne', 'ne', 'sw', 'se', 'nw', 'ne', 'w', 'sw', 'se', 'e', 'nw', 'se', 'se'],
        ['w', 'nw', 'ne', 'se', 'ne', 'se', 'ne', 'nw', 'w', 'ne', 'nw', 'se', 'w', 'e', 'se', 'w', 'se', 'se', 'se', 'w'],
        ['ne', 'ne', 'w', 'sw', 'nw', 'e', 'w', 'sw', 'ne', 'ne', 'se', 'nw', 'ne', 'se', 'w', 'e', 'sw'],
        ['e', 'ne', 'sw', 'nw', 'sw', 'nw', 'se', 'ne', 'nw', 'nw', 'nw', 'w', 'se', 'e', 'sw', 'ne', 'e', 'w', 'se', 'ne', 'se'],
        ['ne', 'sw', 'nw', 'e', 'w', 'nw', 'nw', 'se', 'e', 'nw', 'se', 'e', 'se', 'w', 'se', 'nw', 'sw', 'e', 'e', 'w', 'e'],
        ['w', 'se', 'w', 'e', 'e', 'e', 'nw', 'ne', 'se', 'nw', 'w', 'w', 'sw', 'ne', 'w']
    ],
    'expected_black_tile_count': 10
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    tile_paths = part_1.parse_input(test_case['input'])
    assert_equals(tile_paths, test_case['exepected_tile_paths'])
    tile_states = part_1.flip_all_paths(tile_paths)
    black_tile_count = part_1.count_black_tiles(tile_states)
    assert_equals(black_tile_count, test_case['expected_black_tile_count'])

print("")
print("[[[ SUCCESS ]]]")
print("")
