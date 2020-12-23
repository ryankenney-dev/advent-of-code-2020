import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

cups = part_2.parse_input(message)
for i in range(0, 100):
	cups = part_2.run_cycle(cups)
result = part_2.get_cycle_signature(cups)

print("")
print("[[[ Result: %s ]]]" % result)
print("")
