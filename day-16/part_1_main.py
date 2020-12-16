import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

ticket_data = part_1.parse_message(message)
invalid_field_values = part_1.find_invalid_nearby_ticket_field_values(ticket_data)

print("")
print("[[[ Result: %s ]]]" % sum(invalid_field_values))
print("")
