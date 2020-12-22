import part_2
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
    'expected_to_string': '''..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###''',
    'expected_edges': [
        ( part_2.EDGE_NORTH, '..##.#..#.' ),
        ( part_2.EDGE_EAST, '...#.##..#' ),
        ( part_2.EDGE_SOUTH, '###..###..' ),
        ( part_2.EDGE_WEST, '.#..#####.' ),
    ],
    'expected_after_rotate': '''.#..#####.
.#.####.#.
###...#..#
#..#.##..#
#....#.##.
...##.##.#
.#...#....
#.#.##....
##.###.#.#
#..##.#...''',
    'expected_after_flip': '''.#..#.##..
.....#..##
.#..##...#
#...#.####
.###.##.##
###.#...##
##..#.#.#.
..#....#..
.#.#...###
###..###..''',
    'expected_after_shink': '''#..#....
...##..#
###.#...
#.##.###
#...#.##
#.#.#..#
.#....#.
##...#.#''',
    'find_image_tile': '''Tile 0:
#.#.
###.
..#.
.#.#''',
    'find_image_input': '# #',
    'exected_images_found': [
        (0,0),
        (0,1),
        (1,3),
    ],
    'expected_west_edge_indexes': [
        ( '.#..#####.', part_2.TileOrientation( tile_id=2311, translation_id=0 ) ),
        ( '###..###..', part_2.TileOrientation( tile_id=2311, translation_id=1 ) ),
        ( '...#.##..#', part_2.TileOrientation( tile_id=2311, translation_id=2 ) ),
        ( '..##.#..#.', part_2.TileOrientation( tile_id=2311, translation_id=3 ) ),
        ( '#..##.#...', part_2.TileOrientation( tile_id=2311, translation_id=4 ) ),
        ( '..###..###', part_2.TileOrientation( tile_id=2311, translation_id=5 ) ),
        ( '.#####..#.', part_2.TileOrientation( tile_id=2311, translation_id=6 ) ),
        ( '.#..#.##..', part_2.TileOrientation( tile_id=2311, translation_id=7 ) ),
    ],
    'expected_north_edge_indexes': [
        ( '..##.#..#.', part_2.TileOrientation( tile_id=2311, translation_id=0 ) ),
        ( '.#..#####.', part_2.TileOrientation( tile_id=2311, translation_id=1 ) ),
        ( '###..###..', part_2.TileOrientation( tile_id=2311, translation_id=2 ) ),
        ( '...#.##..#', part_2.TileOrientation( tile_id=2311, translation_id=3 ) ),
        ( '.#..#.##..', part_2.TileOrientation( tile_id=2311, translation_id=4 ) ),
        ( '#..##.#...', part_2.TileOrientation( tile_id=2311, translation_id=5 ) ),
        ( '..###..###', part_2.TileOrientation( tile_id=2311, translation_id=6 ) ),
        ( '.#####..#.', part_2.TileOrientation( tile_id=2311, translation_id=7 ) ),
    ],
    'image_to_find': '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   ''',
    'expected_hash_count': 273
}]

def assert_equals(actual_value, expected_value):
    if actual_value != expected_value:
        raise Exception('Expected %s but saw %s' % (expected_value, actual_value))

for test_case in test_cases:

    tiles = part_2.parse_input(test_case['input'])
    for expected_edge in test_case['expected_edges']:
        assert_equals(part_2.tile_get_edge(tiles[0], expected_edge[0]), expected_edge[1])

    # Test tile_to_string()
    s = part_2.tile_to_string(tiles[0])
    assert_equals(s, test_case['expected_to_string'])

    # Test rotate()
    rotated = part_2.tile_translate(tiles[0], part_2.Translation(rotate=1))
    assert_equals(part_2.tile_to_string(rotated), test_case['expected_after_rotate'])
    # ... verifying the original tile not changed
    for expected_edge in test_case['expected_edges']:
        assert_equals(part_2.tile_get_edge(tiles[0], expected_edge[0]), expected_edge[1])

    # Test flip()
    flipped = part_2.tile_translate(tiles[0], part_2.Translation(flip=1))
    assert_equals(part_2.tile_to_string(flipped), test_case['expected_after_flip'])
    # ... verifying the original tile not changed
    for expected_edge in test_case['expected_edges']:
        assert_equals(part_2.tile_get_edge(tiles[0], expected_edge[0]), expected_edge[1])

    # Test shrink()
    shrunk = part_2.tile_shrink(tiles[0])
    assert_equals(part_2.tile_to_string(shrunk), test_case['expected_after_shink'])
    # ... verifying the original tile not changed
    for expected_edge in test_case['expected_edges']:
        assert_equals(part_2.tile_get_edge(tiles[0], expected_edge[0]), expected_edge[1])

    # Test find_image()
    tile = part_2.tile_create_from_text(test_case['find_image_tile'])
    image = test_case['find_image_input']
    image_results = part_2.tile_find_image(tile, image)
    assert_equals(image_results, test_case['exected_images_found'])

    # Test generate_indexes()
    indexes = part_2.generate_indexes(tiles)
    # ... Verifying north edges
    tile_edges = indexes.edge_indexes[part_2.EDGE_NORTH]
    for expected_index_entry in test_case['expected_north_edge_indexes']:
        if expected_index_entry[0] not in tile_edges:
            raise Exception('Missing expected entry: %s' % expected_index_entry[0])
        if expected_index_entry[1] not in tile_edges[expected_index_entry[0]]:
            raise Exception('Missing expected entry in %s: %s' % (expected_index_entry[0], expected_index_entry[1]))
    # ... Verifying west edges
    tile_edges = indexes.edge_indexes[part_2.EDGE_WEST]
    for expected_index_entry in test_case['expected_west_edge_indexes']:
        if expected_index_entry[0] not in tile_edges:
            raise Exception('Missing expected entry: %s' % expected_index_entry[0])
        if expected_index_entry[1] not in tile_edges[expected_index_entry[0]]:
            raise Exception('Missing expected entry in %s: %s' % (expected_index_entry[0], expected_index_entry[1]))
    # ... Verifying all_tile_orientations
    assert_equals(len(indexes.all_tile_orientations), len(part_2.STANDARD_TRANSLATIONS) * len(tiles))

    # Test get_next_square()
    example_matrix = [[0]*2 for i in range(2)]
    next = part_2.SquareLocation(x=0,y=0)
    next = part_2.get_next_square(next,example_matrix)
    assert_equals(next, part_2.SquareLocation(x=1,y=0))
    next = part_2.get_next_square(next,example_matrix)
    assert_equals(next, part_2.SquareLocation(x=0,y=1))
    next = part_2.get_next_square(next,example_matrix)
    assert_equals(next, part_2.SquareLocation(x=1,y=1))
    next = part_2.get_next_square(next,example_matrix)
    assert_equals(next, None)

    tiles_matrix = part_2.find_assembled_tiles(tiles)
    uber_tile = part_2.join_tiles(tiles_matrix)
    found = part_2.find_image_in_all_tile_translations(uber_tile, test_case['image_to_find'])
    tile = found[0][0]
    for coords in found[0][1]:
        tile = part_2.tile_apply_image(tile, test_case['image_to_find'], coords)
    # print(part_2.tile_to_string(tile))
    hash_count = part_2.tile_count_char(tile, '#')
    assert_equals(hash_count, test_case['expected_hash_count'])

print("")
print("[[[ SUCCESS ]]]")
print("")
