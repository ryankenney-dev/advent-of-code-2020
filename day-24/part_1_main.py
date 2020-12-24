import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

tile_paths = part_1.parse_input(message)
tile_states = part_1.flip_all_paths(tile_paths)
black_tile_count = part_1.count_black_tiles(tile_states)

print("")
print("[[[ Result: %s ]]]" % black_tile_count)
print("")
