import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

cups = part_1.parse_input(message)
for i in range(0, 100):
	cups = part_1.run_cycle(cups)
result = part_1.get_cycle_signature(cups)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
