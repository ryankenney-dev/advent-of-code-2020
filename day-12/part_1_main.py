import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

instructions = part_1.parse_message_to_instructions(message)
distance = part_1.process_instructions_to_manhattan_distance(instructions)

print("")
print("[[[ Distance: %s ]]]" % distance)
print("")
