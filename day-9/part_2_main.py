import part_1
import sys

with open(sys.argv[1], 'r') as f:
    lines = f.read().splitlines()

first_invalid_value = part_1.find_first_invalid_value(lines, int(sys.argv[2]))
contiguous_range = part_1.find_contiguous_range_adding_to(lines, first_invalid_value)
sum = part_1.find_sum_of_min_max_of_contiguous_range_adding_to(lines, first_invalid_value)

print("")
print("[[[ First Invalid Value: %s ]]]" % first_invalid_value)
print("")
print("[[[ Contiguous Range that Sums: %s ]]]" % contiguous_range)
print("")
print("[[[ Sum of Min/Max in Range: %s ]]]" % sum)
print("")
