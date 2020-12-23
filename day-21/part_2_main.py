import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

foods = part_2.parse_input(message)
result = part_2.compute_result(foods)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
