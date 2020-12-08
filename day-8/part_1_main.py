import part_1
import sys

with open(sys.argv[1], 'r') as f:
    program = part_1.parse_program(f.read())

accumulator_value = part_1.execute_and_return_accumulator_on_loop(program)

print("")
print("[[[ Accumulator value: %s ]]]" % accumulator_value)
print("")
