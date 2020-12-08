import part_2

test_cases = [{
	'input': '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6''',
	'expected_program': [
		{'operation': 'nop', 'argument': 0},
		{'operation': 'acc', 'argument': 1},
		{'operation': 'jmp', 'argument': 4},
		{'operation': 'acc', 'argument': 3},
		{'operation': 'jmp', 'argument': -3},
		{'operation': 'acc', 'argument': -99},
		{'operation': 'acc', 'argument': 1},
		{'operation': 'jmp', 'argument': -4},
		{'operation': 'acc', 'argument': 6}
	],
	'expected_toggle_line': 7,
	'expected_accumulator_value': 8

}]

for test_case in test_cases:
	program = part_2.parse_program(test_case['input'])
	print(program)
	if program != test_case['expected_program']:
		raise Exception('Unexpected')
	toggle_line = part_2.find_op_toggle_line_that_prevents_loop(program)
	if toggle_line != test_case['expected_toggle_line']:
		raise Exception('Unexpected')
	modified_program = part_2.create_toggled_prog(program, toggle_line)
	print(modified_program)
	accumulator_value = part_2.execute_and_return_accumulator(modified_program)
	if accumulator_value != test_case['expected_accumulator_value']:
		raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
