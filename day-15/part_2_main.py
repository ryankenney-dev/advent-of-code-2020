import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

numbers = part_2.parse_to_numbers(message)
result = part_2.compute_until(numbers, 30000000)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
