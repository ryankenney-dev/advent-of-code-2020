import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

instructions = part_2.parse_message_to_instructions(message)
distance = part_2.process_instructions_to_manhattan_distance(instructions)

print("")
print("[[[ Distance: %s ]]]" % distance)
print("")
