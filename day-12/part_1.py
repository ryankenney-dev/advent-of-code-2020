import re

CARDINAL_INCREMENTS = {
	'N': (0,-1),
	'E': (1,0),
	'S': (0,1),
	'W': (-1,0),
}

CARDINAL_SERIES = [
	CARDINAL_INCREMENTS['E'],
	CARDINAL_INCREMENTS['S'],
	CARDINAL_INCREMENTS['W'],
	CARDINAL_INCREMENTS['N'],
]

TURN_DIRECTION_MULTIPLIERS = {
	'R': 1,
	'L': -1,
}

def get_new_heading(heading, turn_direction, turn_degrees):
	return int((heading + TURN_DIRECTION_MULTIPLIERS[turn_direction] * turn_degrees/90) % len(CARDINAL_SERIES))

def get_cardinal_new_location(location, move_direction, move_amount):
	return ( \
		location[0] + CARDINAL_INCREMENTS[move_direction][0] * move_amount, \
		location[1] + CARDINAL_INCREMENTS[move_direction][1] * move_amount )

def get_relative_new_location(location, heading, move_amount):
	return ( \
		location[0] + CARDINAL_SERIES[heading][0] * move_amount, \
		location[1] + CARDINAL_SERIES[heading][1] * move_amount )

def parse_message_to_instructions(message):
	instructions = []
	for line in message.splitlines():
		match = re.match(r'^([NSEWLRF])(\d+)$', line)
		if not match:
			raise Exception('Invalid instruction: %s' % line)
		instructions.append({
			'action': match.group(1),
			'amount': int(match.group(2)),
		})
	return instructions

def process_instructions_to_manhattan_distance(instructions):
	location = (0,0)
	heading = 0
	for instruction in instructions:
		action = instruction['action']
		amount = instruction['amount']
		if action in ('N','S','E','W'):
			location = get_cardinal_new_location(location, action, amount)
		elif action in ('R', 'L'):
			heading = get_new_heading(heading, action, amount)
		elif action == 'F':
			location = get_relative_new_location(location, heading, amount)
		else:
			raise Exception('Invalid instruction: %s' % instruction)

	return abs(location[0]) + abs(location[1])