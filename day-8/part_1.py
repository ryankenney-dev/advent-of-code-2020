import regex

def parse_program(source_code):
	instruction_pattern = regex.compile(r'^(nop|acc|jmp) ([\-+])(\d+)$')
	instructions = []
	for line in source_code.splitlines():
		match = instruction_pattern.match(line)
		if not match:
			raise Exception('Invalid instruction: %s' % line)
		if match.group(2) == '-':
			sign_value = -1
		else:
			sign_value = 1
		instructions.append({
			'operation': match.group(1),
			'argument': sign_value*int(match.group(3))
		})
	return instructions

def execute_and_return_accumulator_on_loop(program):
	accumulator = 0
	line = 0
	lines_hit = set()
	while line not in lines_hit:
		lines_hit.add(line)
		instruction = program[line]
		print (instruction)
		if instruction['operation'] == 'jmp':
			line_offset = instruction['argument']
		elif instruction['operation'] == 'nop':
			line_offset = 1
		elif instruction['operation'] == 'acc':
			accumulator = accumulator + instruction['argument']
			line_offset = 1
		else:
			raise Exception('Unrecognized instruction')
		line = line + line_offset
	return accumulator