import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

instructions = part_1.parse_to_instructions(message)
memory = part_1.execute_instructions(instructions)
sum_of_memory = part_1.sum_of_memory(memory)

print("")
print("[[[ Sum of Memory: %s ]]]" % sum_of_memory)
print("")
