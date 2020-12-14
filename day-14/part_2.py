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
	mask = '0'.zfill(36)
	memory = {}
	for instruction in instructions:
		if instruction['action'] == 'set_mask':
			mask = instruction['value']
		elif instruction['action'] == 'write':
			memory_locations = get_memory_locations(mask, instruction)
			for memory_location in memory_locations:
				memory[memory_location] = instruction['value']
		else:
			raise Exception('Invalid instruction: %s' % instruction)
	return memory

def sum_of_memory(memory):
	return sum(memory.values())

def apply_mask(mask, value):
	new_value = list(int_to_bin(value))
	for i in range(0,len(mask)):
		c = mask[i]
		if c == 'X' or c == '1':
			new_value[i] = c
	return ''.join(new_value)

def get_memory_locations(mask, instruction):
	location = apply_mask(mask, instruction['location'])
	x_indexes = get_x_indexes(location)
	memory_locations = []
	# Walk every permutation of Xs by iterating
	# through integers and convertng to binary
	for i in range(0, pow(2, len(x_indexes))):
		# To bin string, then reverse, then chop to length
		b = int_to_bin(i)[::-1][0:len(x_indexes)]
		l = list(location)
		for x in range(0, len(x_indexes)):
			l[x_indexes[x]] = b[x]
		memory_locations.append(''.join(l))
	return memory_locations

def get_x_indexes(value):
	x_indexes = []
	for i in range(0, len(value)):
		c = value[i]
		if c == 'X':
			x_indexes.append(i)
	return x_indexes

def int_to_bin(i):
	return str(bin(i))[2:].zfill(36)

def bin_to_int(b):
	return int(b, 2)
