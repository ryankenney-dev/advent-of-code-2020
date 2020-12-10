import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

jolt_adapters = part_1.parse_jolt_adapters(message)
differences = part_1.count_jolt_differences(jolt_adapters)
product = part_1.product_of_1_and_3_jolt_differences(jolt_adapters)

print("")
print("[[[ Jolt Difference Counts: %s ]]]" % differences)
print("")
print("[[[ Product Total 1 and 3 Jolt Differences: %s ]]]" % product)
print("")
