import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

parsed_cubes = part_1.parse_to_active_cubes(message)
active_cubes = part_1.process_6_cycles(parsed_cubes)

print("")
print("[[[ Active Cubes: %s ]]]" % len(active_cubes))
print("")
