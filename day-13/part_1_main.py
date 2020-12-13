import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

notes = part_1.parse_message_to_notes(message)
bus = part_1.find_bus_with_minimum_wait(notes)
result = part_1.compute_result(notes)

print("")
print("[[[ Earliest Bus: %s ]]]" % str(bus))
print("")
print("[[[ Result: %s ]]]" % result)
print("")
