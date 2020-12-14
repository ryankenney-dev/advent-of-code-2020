import re

def parse_to_instructions(message):
	mask_pattern = re.compile(r'mask = ([X01]+)')
	write_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
	lines = message.splitlines()
	instructions = []
	for line in lines:
		match = mask_pattern.match(line)
		if match:
			instructions.append({ 'action': 'set_mask', 'value': match.group(1) })
			continue
		match = write_pattern.match(line)
		if match:
			instructions.append({ 'action': 'write', 'location': int(match.group(1)), 'value': int(match.group(2)) })
			continue
		raise Exception('Invalid line: %s' % line)
	return instructions

def execute_instructions(instructions):
	mask = 'X'.zfill(36)
	memory = {}
	for instruction in instructions:
		if instruction['action'] == 'set_mask':
			mask = instruction['value']
		elif instruction['action'] == 'write':
			memory[instruction['location']] = apply_mask(mask, instruction['value'])
		else:
			raise Exception('Invalid instruction: %s' % instruction)
	return memory

def sum_of_memory(memory):
	return sum(map(lambda v: bin_to_int(v), memory.values()))

def apply_mask(mask, value):
	new_value = list(int_to_bin(value))
	for i in range(0,len(mask)):
		c = mask[i]
		if c == '0' or c == '1':
			new_value[i] = c
	return ''.join(new_value)

def int_to_bin(i):
	return str(bin(i))[2:].zfill(36)

def bin_to_int(b):
	return int(b, 2)
