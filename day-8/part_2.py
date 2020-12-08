import regex
import copy

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

def execute_and_return_hits_infinite_loop(program):
	accumulator = 0
	line = 0
	lines_hit = set()
	while line < len(program) and line not in lines_hit:
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
	return line in lines_hit

def execute_and_return_accumulator(program):
	accumulator = 0
	line = 0
	lines_hit = set()
	while line < len(program) and line not in lines_hit:
		print("LINE: %s" % line)
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
	if line in lines_hit:
		raise Exception('Loop detected')
	return accumulator

def find_op_toggle_line_that_prevents_loop(program):
	for l in range(0,len(program)):
		line = program[l]
		if line['operation'] == 'acc':
			continue
		modified_program = create_toggled_prog(program, l)
		if not execute_and_return_hits_infinite_loop(modified_program):
			return l
	raise Exception('No solution found')

def create_toggled_prog(program, line_number):
	program_copy = copy.deepcopy(program)
	if program_copy[line_number]['operation'] == 'jmp':
		program_copy[line_number]['operation'] = 'nop'
	elif program_copy[line_number]['operation'] == 'nop':
		program_copy[line_number]['operation'] = 'jmp'
	else:
		raise Exception('Invalid op to toggle')
	return program_copy

