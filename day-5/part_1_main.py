import part_1
import sys

max_seat_id = 0
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        seat_id = part_1.get_seat_id(line)
        if seat_id > max_seat_id:
            max_seat_id = seat_id

print("----")
print("Max seat id: %s" % max_seat_id)
