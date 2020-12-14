import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

instructions = part_2.parse_to_instructions(message)
memory = part_2.execute_instructions(instructions)
sum_of_memory = part_2.sum_of_memory(memory)

print("")
print("[[[ Sum of Memory: %s ]]]" % sum_of_memory)
print("")
