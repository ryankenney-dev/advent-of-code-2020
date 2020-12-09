import part_1
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

first_invalid_value = part_1.find_first_invalid_value(lines, int(sys.argv[2]))

print("")
print("[[[ First Invalid Value: %s ]]]" % first_invalid_value)
print("")
