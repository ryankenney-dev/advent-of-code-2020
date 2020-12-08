import part_2
import sys

with open(sys.argv[1], 'r') as f:
    program = part_2.parse_program(f.read())

toggle_line = part_2.find_op_toggle_line_that_prevents_loop(program)

print("Toggle line: %s" % toggle_line)

modified_program = part_2.create_toggled_prog(program, toggle_line)

accumulator_value = part_2.execute_and_return_accumulator(modified_program)

print("")
print("[[[ Accumulator value: %s ]]]" % accumulator_value)
print("")
