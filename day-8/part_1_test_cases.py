import part_1
import json

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
	'expected_accumulator_value': 5

}]

for test_case in test_cases:
	program = part_1.parse_program(test_case['input'])
	print(program)
	if program != test_case['expected_program']:
		raise Exception('Unexpected')
	accumulator_value = part_1.execute_and_return_accumulator_on_loop(program)
	print(accumulator_value)
	if accumulator_value != test_case['expected_accumulator_value']:
		raise Exception('Unexpected')


print("")
print("[[[ SUCCESS ]]]")
print("")
