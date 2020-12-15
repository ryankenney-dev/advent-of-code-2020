import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

numbers = part_1.parse_to_numbers(message)
result = part_1.compute_until_2020(numbers)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
