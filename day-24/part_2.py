import regex

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

def get_tile_coord_in_direction(coord, direction):
	if direction == 'e':
		return (coord[0]+1, coord[1])
	if direction == 'w':
		return (coord[0]-1, coord[1])
	elif direction == 'ne':
		return (coord[0], coord[1]+1)
	elif direction == 'sw':
		return (coord[0], coord[1]-1)
	elif direction == 'nw':
		return (coord[0]-1, coord[1]+1)
	elif direction == 'se':
		return (coord[0]+1, coord[1]-1)
	else:
		raise Exception('Invalid direction: %s' % direction)


TILE_STATES = ['black', 'white']

def flip_all_paths(tile_paths):
	tile_states = {}
	for tile_path in tile_paths:
		coords = get_tile_coords(tile_path)
		# True == white
		if coords not in tile_states:
			tile_states[coords] = 'black'
		else:
			tile_states[coords] = (TILE_STATES.index(tile_states[coords]) + 1) % len(tile_states)
	return tile_states

def count_black_tiles(tile_states):
	count = 0
	for state in tile_states.values():
		if state == 'black':
			count += 1
	return count

# def get_grid_bounds(tile_states):
# 	absmax = sys.maxsize
# 	absmin = -sys.maxsize - 1
#     x_range = (absmax, absmin)
#     y_range = (absmax, absmin)
# 	for key in tile_states.keys():
# 		x_range = (min(x_range[0], key[0]), max(x_range[1], key[0]))
# 		y_range = (min(y_range[0], key[1]), max(y_range[1], key[1]))
# 	return { 'x': x_range, 'y': y_range }

# def get_state_changes(tile)


# # . Find grid bounds
# # . Grow grid bounds by 1 in all 3 dimensions
# # . Walk grid, testing for state changes
# # . Apply new states

