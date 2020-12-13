import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

buses = part_2.parse_to_buses(message)
timestamp = part_2.find_time_with_bus_offsets(buses)

print("")
print("[[[ Timestamp: %s ]]]" % timestamp)
print("")
