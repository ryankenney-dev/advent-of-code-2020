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

def rotate_relative_location(direction, center, location):
	turn_multipliers = {
		'R': (-1,1),
		'L': (1,-1),
	}
	# General logic: find relative offset, flip x/y offets,
	# and flip the sign of one (depending upon right/left turn)
	relative_location = (location[0] - center[0], location[1] - center[1])
	return (\
		center[0] + (turn_multipliers[direction][0] * relative_location[1]), \
		center[1] + (turn_multipliers[direction][1] * relative_location[0]))

def get_new_heading(heading, turn_direction, turn_degrees):
	multipliers = {
		'R': 1,
		'L': -1,
	}
	return int((heading + multipliers[turn_direction] * turn_degrees/90) % len(CARDINAL_SERIES))

def get_cardinal_new_location(location, move_direction, move_amount):
	return ( \
		location[0] + CARDINAL_INCREMENTS[move_direction][0] * move_amount, \
		location[1] + CARDINAL_INCREMENTS[move_direction][1] * move_amount )

def get_ship_relative_move(location, waypoint_location, multiplier):
	return ( \
		(waypoint_location[0] - location[0]) * multiplier, \
		(waypoint_location[1] - location[1]) * multiplier \
	)

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

def process_one_instruction(instruction, state):
	action = instruction['action']
	amount = instruction['amount']
	if action in ('N','S','E','W'):
		state.waypoint_location = get_cardinal_new_location(state.waypoint_location, action, amount)
	elif action in ('R', 'L'):
		# Rotate the waypoint location around the ship
		for turn in range(0,int(amount/90)):
			state.waypoint_location = rotate_relative_location(action, state.location, state.waypoint_location)
		# Update waypoint heading
		waypoint_heading = get_new_heading(state.waypoint_heading, action, amount)
	elif action == 'F':
		move = get_ship_relative_move(state.location, state.waypoint_location, amount)
		state.location = (state.location[0] + move[0], state.location[1] + move[1])
		state.waypoint_location = (state.waypoint_location[0] + move[0], state.waypoint_location[1] + move[1])
	else:
		raise Exception('Invalid instruction: %s' % instruction)

def process_instructions_to_manhattan_distance(instructions):
	class state:
		location = (0,0)
		waypoint_heading = 0
		waypoint_location = (10,-1)
	for instruction in instructions:
		process_one_instruction(instruction, state)
	return abs(state.location[0]) + abs(state.location[1])