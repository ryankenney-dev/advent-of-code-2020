import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

tile_paths = part_2.parse_input(message)
tile_states = part_2.flip_all_paths(tile_paths)
for i in range(0, 100):
    part_2.run_cycle(tile_states)
black_tile_count = part_2.count_black_tiles(tile_states)

print("")
print("[[[ Result: %s ]]]" % black_tile_count)
print("")
