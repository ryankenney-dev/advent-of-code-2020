import part_2
import sys
import json

with open(sys.argv[1], 'r') as f:
    message = f.read()

jolt_adapters = part_2.parse_jolt_adapters(message)
#combinations = part_2.find_all_combinations(jolt_adapters)
combinations_count = part_2.count_all_combinations(jolt_adapters)

print("")
#print("[[[ Adapter Combinations: %s ]]]" % combinations)
print("[[[ Adapter Combinations: %s ]]]" % combinations_count)
print("")
