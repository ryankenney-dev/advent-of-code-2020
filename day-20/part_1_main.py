import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

tiles = part_1.parse_input(message)
corners_product = part_1.find_solution(tiles)

print("")
print("[[[ Corners Product: %s ]]]" % corners_product)
print("")
