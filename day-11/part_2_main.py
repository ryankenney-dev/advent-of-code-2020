import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

seats = part_2.parse_to_seats_array(message)
occupied_count = part_2.process_until_stable_return_occupied_count(seats)

print("")
print("[[[ Occupied Count: %s ]]]" % occupied_count)
print("")
