import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

tiles = part_2.parse_input(message)
corners_product = part_2.find_solution(tiles)

print("")
print("[[[ Corners Product: %s ]]]" % corners_product)
print("")
