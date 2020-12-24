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
	x = 0
	y = 0
	for direction in tile_path:
		if direction == 'e':
			x += 1
		if direction == 'w':
			x -= 1
		elif direction == 'ne':
			y += 1
		elif direction == 'sw':
			y -= 1
		elif direction == 'nw':
			y += 1
			x -= 1
		elif direction == 'se':
			y -= 1
			x += 1
	return (x,y)

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