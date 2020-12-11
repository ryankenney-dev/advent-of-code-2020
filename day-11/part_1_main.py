import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

seats = part_1.parse_to_seats_array(message)
occupied_count = part_1.process_until_stable_return_occupied_count(seats)

print("")
print("[[[ Occupied Count: %s ]]]" % occupied_count)
print("")
