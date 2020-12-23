import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

foods = part_1.parse_input(message)
result = part_1.compute_result(foods)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
