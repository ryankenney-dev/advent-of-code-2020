import regex
import sys

directions_regex = regex.compile(r'^(e|se|sw|w|nw|ne)+$')

def parse_input(message):
	tile_paths = []
	lines = message.splitlines()
	for line in lines:
		match = directions_regex.match(line)
		if not match:
			raise Exception('Invalid input line: %s' % line)
		tile_paths.append(match.captures(1))
	return tile_paths

# It turns out we can model a hex grid as a square grid (visually squished),
# but where one of the two diagonal directions are connected.
def get_tile_coords(tile_path):
	coords = (0,0)
	for direction in tile_path:
		coords = get_tile_coord_in_direction(coords, direction)
	return coords

def get_tile_coord_in_direction(coords, direction):
	if direction == 'e':
		return (coords[0]+1, coords[1])
	if direction == 'w':
		return (coords[0]-1, coords[1])
	elif direction == 'ne':
		return (coords[0], coords[1]-1)
	elif direction == 'sw':
		return (coords[0], coords[1]+1)
	elif direction == 'nw':
		return (coords[0]-1, coords[1]-1)
	elif direction == 'se':
		return (coords[0]+1, coords[1]+1)
	else:
		raise Exception('Invalid direction: %s' % direction)

def get_all_neighbor_coords(coords):
	neighbors = []
	for direction in ['ne', 'e', 'se', 'sw', 'w', 'nw']:
		neighbors.append(get_tile_coord_in_direction(coords, direction))
	return neighbors

TILE_STATES = ['black', 'white']

def get_color(coords, tile_states):
	if coords not in tile_states:
		return 'white'
	else:
		return tile_states[coords]

def set_color(coords, color, tile_states):
	if color == 'white' and coords not in tile_states:
		# No need to create an entry. Presume white if non-exist.
		return
	else:
		tile_states[coords] = color

def flip_all_paths(tile_paths):
	tile_states = {}
	for tile_path in tile_paths:
		coords = get_tile_coords(tile_path)
		if coords not in tile_states:
			tile_states[coords] = 'black'
		else:
			previous_color = tile_states[coords]
			if previous_color == 'black':
				tile_states[coords] = 'white'
			else:
				tile_states[coords] = 'black'
	return tile_states

def count_black_tiles(tile_states):
	count = 0
	for state in tile_states.values():
		if state == 'black':
			count += 1
	return count

def get_grid_bounds(tile_states):
	absmax = sys.maxsize
	absmin = -sys.maxsize - 1
	x_range = (absmax, absmin)
	y_range = (absmax, absmin)
	for key in tile_states.keys():
		x_range = (min(x_range[0], key[0]), max(x_range[1], key[0]))
		y_range = (min(y_range[0], key[1]), max(y_range[1], key[1]))
	return { 'x': x_range, 'y': y_range }

def grow_bounds(bounds):
	return {
		'x': (bounds['x'][0]-1, bounds['x'][1]+1),
		'y': (bounds['y'][0]-1, bounds['y'][1]+1),
	}

def walk_grid(bounds, callback):
	for y in range(bounds['y'][0], bounds['y'][1]+1):
		for x in range(bounds['x'][0], bounds['x'][1]+1):
			callback((x,y))

def get_adjacent_black(coords, tile_states):
	black_count = 0
	neighbors_coords = get_all_neighbor_coords(coords)
	for neighbor_coords in neighbors_coords:
		color = get_color(neighbor_coords, tile_states)
		if color == 'black':
			black_count += 1
	return black_count

def get_all_state_changes(tile_states):
	bounds = get_grid_bounds(tile_states)
	bounds = grow_bounds(bounds)
	state_changes = []
	def identify_change(coords):
		nonlocal tile_states
		nonlocal state_changes
		color = get_color(coords, tile_states)
		black_count = get_adjacent_black(coords, tile_states)

		# "Any black tile with zero or more than 2 black tiles
		# immediately adjacent to it is flipped to white."
		if color == 'black' and (black_count == 0 or black_count > 2):
			state_changes.append({'coords': coords, 'color': 'white'})
		# "Any white tile with exactly 2 black tiles immediately
		# adjacent to it is flipped to black"
		elif color == 'white' and black_count == 2:
			state_changes.append({'coords': coords, 'color': 'black'})

	walk_grid(bounds, identify_change)
	return state_changes

def apply_state_changes(state_changes, tile_states):
	for state_change in state_changes:
		set_color(state_change['coords'], state_change['color'], tile_states)

def run_cycle(tile_states):
	state_changes = get_all_state_changes(tile_states)
	apply_state_changes(state_changes, tile_states)

def state_to_string(tile_states):
	bounds = get_grid_bounds(tile_states)
	bounds = grow_bounds(bounds)
	width = bounds['x'][1] - bounds['x'][0] + 1
	height = bounds['y'][1] - bounds['y'][0] + 1
	grid = [[['?']]*width for i in range(height)]
	def append_tile(coords):
		nonlocal tile_states
		nonlocal bounds
		if 'black' == get_color(coords, tile_states):
			color = 'X'
		else:
			color = '.'
		grid[coords[1]-bounds['y'][0]][coords[0]-bounds['x'][0]] = color
	walk_grid(bounds, append_tile)
	return '\n'.join(list(map(lambda l: ''.join(map(lambda c: str(c), l)), grid)))
