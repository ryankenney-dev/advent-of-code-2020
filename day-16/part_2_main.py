import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

ticket_data = part_2.parse_message(message)
product_departure_fields = part_2.compute_product_departure_fields(ticket_data)

print("")
print("[[[ Product: %s ]]]" % product_departure_fields)
print("")
