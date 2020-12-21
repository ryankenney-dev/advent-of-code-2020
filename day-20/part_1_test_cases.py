import part_1
import re

test_cases = [{
    'input': '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...''',
    'expected_edges': [
        ( part_1.EDGE_NORTH, '..##.#..#.' ),
        ( part_1.EDGE_EAST, '...#.##..#' ),
        ( part_1.EDGE_SOUTH, '###..###..' ),
        ( part_1.EDGE_WEST, '.#..#####.' ),
    ],
    'expected_edges_after_rotate': [
        ( part_1.EDGE_NORTH, '.#..#####.' ),
        ( part_1.EDGE_EAST, '..##.#..#.' ),
        ( part_1.EDGE_SOUTH, '...#.##..#' ),
        ( part_1.EDGE_WEST, '###..###..' ),
    ],
    'expected_edges_after_flip': [
        ( part_1.EDGE_NORTH, '.#..#.##..' ),
        ( part_1.EDGE_EAST, '.#####..#.' ),
        ( part_1.EDGE_SOUTH, '..###..###' ),
        ( part_1.EDGE_WEST, '#..##.#...' ),
    ],
    'expected_west_edge_indexes': [
        ( '.#..#####.', ( 2311, {'rotate': 0} ) ),
        ( '###..###..', ( 2311, {'rotate': 1} ) ),
        ( '...#.##..#', ( 2311, {'rotate': 2} ) ),
        ( '..##.#..#.', ( 2311, {'rotate': 3} ) ),
        ( '#..##.#...', ( 2311, {'flip': 1, 'rotate': 0} ) ),
        ( '..###..###', ( 2311, {'flip': 1, 'rotate': 1} ) ),
        ( '.#####..#.', ( 2311, {'flip': 1, 'rotate': 2} ) ),
        ( '.#..#.##..', ( 2311, {'flip': 1, 'rotate': 3} ) ),
    ],
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    tiles = part_1.parse_input(test_case['input'])
    for expected_edge in test_case['expected_edges']:
        assert_equals(tiles[0].get_edge(expected_edge[0]), expected_edge[1])

    # Test rotate()
    rotated = tiles[0].translate({'rotate': 1})
    for expected_edge in test_case['expected_edges_after_rotate']:
        assert_equals(rotated.get_edge(expected_edge[0]), expected_edge[1])
    # ... verifying the original tile not changed
    for expected_edge in test_case['expected_edges']:
        assert_equals(tiles[0].get_edge(expected_edge[0]), expected_edge[1])

    # Test flip()
    flipped = tiles[0].translate({'flip': 1})
    for expected_edge in test_case['expected_edges_after_flip']:
        assert_equals(flipped.get_edge(expected_edge[0]), expected_edge[1])
    # ... verifying the original tile not changed
    for expected_edge in test_case['expected_edges']:
        assert_equals(tiles[0].get_edge(expected_edge[0]), expected_edge[1])

    west_tile_edges = part_1.index_all_west_tile_edges(tiles)
    for expected_index_entry in test_case['expected_west_edge_indexes']:
        if expected_index_entry[0] not in west_tile_edges:
            raise Exception('Missing expected entry: %s' % expected_index_entry[0])
        if expected_index_entry[1] not in west_tile_edges[expected_index_entry[0]]:
            raise Exception('Missing expected entry in %s: %s' % (expected_index_entry[0], expected_index_entry[1]))

print("")
print("[[[ SUCCESS ]]]")
print("")
