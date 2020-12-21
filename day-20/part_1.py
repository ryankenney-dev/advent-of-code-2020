import re
import collections
import copy
import math

tile_id_regex = re.compile(r'^Tile (\d+):$')

EDGE_NORTH=0
EDGE_EAST=1
EDGE_SOUTH=2
EDGE_WEST=3

Tile = collections.namedtuple('Tile', ['tile_id', 'edges'])

def tile_create_from_text(text):
	lines = text.splitlines()
	match = tile_id_regex.match(lines[0])
	tile_id = int(match.group(1))
	north = lines[1]
	south = lines[-1][::-1]
	west = []
	east = []
	for line in lines[1:]:
		east.append(line[-1])
		west.insert(0, line[0])
	east = ''.join(east)
	west = ''.join(west)
	return Tile(tile_id, [north, east, south, west])

def tile_get_edge(tile, direction):
	'''
	Returns the edge signature, in clockwise direction across it.
	'''
	return tile.edges[direction]

def tile_translate(tile, translation):
	'''
	Returns a copy of the Tile, but flipped left-to-right,
	then rotated 90 degrees clockwise by the number of times
	specified in the translation object
	'''
	new_tile = copy.deepcopy(tile)
	new_edges = new_tile.edges

	for i in range(0, translation.flip):
		# Reverse each edge
		for i in range(0, len(new_edges)):
			new_edges[i] = new_edges[i][::-1]
		# Update edge order
		east = new_edges[EDGE_EAST]
		new_edges[EDGE_EAST] = new_edges[EDGE_WEST]
		new_edges[EDGE_WEST] = east

	for i in range(0, translation.rotate):
		new_edges.insert(0, new_edges.pop())

	return new_tile

def tile_to_string(tile):
	width = len(tile.edges[EDGE_NORTH])
	s = tile.edges[EDGE_NORTH] + '\n'
	for i in range(1, width-1):
		s += tile.edges[EDGE_WEST][-1*i-1]
		s += ' ' * (width-2)
		s += tile.edges[EDGE_EAST][i]
		s += '\n'
	s += tile.edges[EDGE_SOUTH][::-1]
	return s

def parse_input(message):
	tile_parts = message.split('\n\n')
	return list(map(lambda t: tile_create_from_text(t), tile_parts))

Translation = collections.namedtuple('Translation', ['flip', 'rotate'])
Translation.__new__.__defaults__ = (0,0)

STANDARD_TRANSLATIONS = [
	Translation(rotate=0),
	Translation(rotate=1),
	Translation(rotate=2),
	Translation(rotate=3),
	Translation(flip=1, rotate=0),
	Translation(flip=1, rotate=1),
	Translation(flip=1, rotate=2),
	Translation(flip=1, rotate=3),
]

TileOrientation = collections.namedtuple('TileOrientation', ['tile_id', 'translation_id'])

TileIndexes = collections.namedtuple('TileIndexes', ['id_index', 'all_tile_orientations', 'edge_indexes'])

def generate_indexes(tiles):
	indexes = TileIndexes(id_index={}, all_tile_orientations=set(), edge_indexes={})
	all_tile_orientations = indexes.all_tile_orientations
	indexes.edge_indexes[EDGE_NORTH] = {}
	north_edges = indexes.edge_indexes[EDGE_NORTH]
	indexes.edge_indexes[EDGE_WEST] = {}
	west_edges = indexes.edge_indexes[EDGE_WEST]

	for tile in tiles:
		for translation_id in range(0, len(STANDARD_TRANSLATIONS)):
			translation = STANDARD_TRANSLATIONS[translation_id]
			translated = tile_translate(tile, translation)
			tile_orientation = TileOrientation(tile.tile_id, translation_id)
			
			indexes.id_index[tile.tile_id] = tile
			all_tile_orientations.add(tile_orientation)
			# NOTE: We only really need to index on of these an apply a translation
			# for my own readability, I'm keeping both for now
			add_to_edge_index(tile_get_edge(translated, EDGE_NORTH), north_edges, tile_orientation)
			add_to_edge_index(tile_get_edge(translated, EDGE_WEST), west_edges, tile_orientation)

	return indexes


def add_to_edge_index(edge, edge_index, tile_orientation):
	if edge not in edge_index:
		edge_index[edge] = set()
	edge_index[edge].add(tile_orientation)

def get_next_square(current_square, solution_matrix, offset=1): 
	'''
	Returns the next square in the matrix,
	walking east across items and south across rows.
	Specify offset=-1 to increment backwards
	'''

	# TODO: Remvoe debug
	# print(solution_matrix)
	# print('type: %s' % type(solution_matrix))

	height = len(solution_matrix)
	width = len(solution_matrix[0])
	square_number = current_square.y * height + current_square.x
	square_number += offset
	new_square = SquareLocation(x=square_number % width, y=int(square_number / width))
	if new_square.y+1 > height:
		return None
	return new_square

def get_compatible_tiles(target_square, solution_matrix, indexes):

	def get_edge_compatible_tiles(edge_direction, adjacent_square):
		'''
		Returns a set of TileOrientations with west edges compatible
		with the existing solution matrix
		'''
		adjacent_tile = get_current_tile(adjacent_square, solution_matrix, indexes)
		# Flip 180 to get complimentary edge from the adjacent tile
		adjacent_tile = tile_translate(adjacent_tile, Translation(rotate=2))
		required_edge = tile_get_edge(adjacent_tile, edge_direction)
		# Reverse direction of edge to translate from adjacent tile
		required_edge = required_edge[::-1]

		print('required_edge: %s' % required_edge)

		if required_edge not in indexes.edge_indexes[edge_direction]:
			return set()
		return indexes.edge_indexes[edge_direction][required_edge]

	tiles_in_use = get_all_current_tile_ids(target_square, solution_matrix, indexes)

	if target_square.x == 0:
		west_compatible = indexes.all_tile_orientations
	else:
		west_compatible = get_edge_compatible_tiles(EDGE_WEST, \
			SquareLocation(target_square.x-1, target_square.y))
	if target_square.y == 0:
		north_compatible = indexes.all_tile_orientations
	else:
		north_compatible = get_edge_compatible_tiles(EDGE_NORTH, \
			SquareLocation(target_square.x, target_square.y-1))

	# TODO: Removed debug
# 	test_tile='''#...##.#..
# .        #
# .        .
# #        .
# .        #
# .        #
# #        #
# .        #
# #        #
# #.##...##.'''
# 	west_square = SquareLocation(target_square.x-1, target_square.y)
# 	if target_square.x > 0:
# 		west_tile = get_current_tile(west_square, solution_matrix, indexes)
# 		if tile_to_string(west_tile) == test_tile and \
# 			west_tile.tile_id == 1951 and \
# 			west_square == SquareLocation(0,0):
# 			print(tile_to_string(west_tile))
# 			print('WEST_INDEXES:%s' % indexes.edge_indexes[EDGE_WEST])
# 			print('WEST C: %s' % west_compatible)
# 			print('NORTH C: %s' % north_compatible)
# 			raise Exception('Wait up')

	compatible_tiles = north_compatible.intersection(west_compatible)
	return filter(lambda t: t.tile_id not in tiles_in_use, compatible_tiles)


SolutionMatrix = collections.namedtuple('SolutionMatrix', ['squares'])
SquareLocation = collections.namedtuple('SquareLocation', ['x', 'y'])

def find_solution(tiles):

	indexes = generate_indexes(tiles)

	width = int(math.sqrt(len(tiles)))
	solution_matrix = [[[]]*width for i in range(width)]
	# Initialize first square with all possible tile orientations
	solution_matrix[0][0] = list(indexes.all_tile_orientations)
	current_square = SquareLocation(0,0)


	# TODO: Remove debug
	# cycle_limit = 20

	while True:

		# TODO: Remove debug
		print('')
		print_matrix_counts(solution_matrix)
		print('current_square: %s' % str(current_square))

		# TODO: Remove debug
		# if cycle_limit < 1:
		# 	break
		# cycle_limit -= 1

		next_square = get_next_square(current_square, solution_matrix)
		if next_square == None:
			# We hit the end of the matrix (we're done)
			break

		# TODO: Remove debug
		print('next_square: %s' % str(next_square))

		next_compatible_tiles = list(get_compatible_tiles(next_square, solution_matrix, indexes))
		solution_matrix[next_square.y][next_square.x] = next_compatible_tiles

		if len(next_compatible_tiles) < 1:

			# TODO: Remove debug
			print('No Solution Found')

			solution_matrix[current_square.y][current_square.x].pop()

			# TODO: Remove debug
			print('Walked back')

			# Walk backwards through all exhasted previous squares
			while len(solution_matrix[current_square.y][current_square.x]) < 1:
				if current_square == SquareLocation(0,0):
					# Should not happen
					raise Exception('No solution found')

				current_square = get_next_square(current_square, solution_matrix, offset=-1)
				# The top item in this just failed
				solution_matrix[current_square.y][current_square.x].pop()

				# TODO: Remove debug
				print('Walked back')

		else:

			# TODO: Remove debug
			print('Found %s Solutions, added to %s' % (len(next_compatible_tiles), next_square))

			current_square = next_square

	print_matrix_ids(solution_matrix)

def get_current_tile(square, solution_matrix, indexes):
	'''
	Returns the tile from the top of the possilbe solutions for the specified square,
	with any translation applied.
	'''

	tile_orientation = solution_matrix[square.y][square.x][-1]

	# TODO: Remove debug
	print('square: %s' % str(square))
	print(len(solution_matrix))
	print(len(solution_matrix[0]))
	print(STANDARD_TRANSLATIONS[tile_orientation.translation_id])

	return tile_translate( \
		indexes.id_index[tile_orientation.tile_id], \
		STANDARD_TRANSLATIONS[tile_orientation.translation_id])

def get_all_current_tile_ids(next_square, solution_matrix, indexes):
	'''
	Returns the set of all tile in use by every square preceeding
	the specified "next" one
	'''
	tile_ids = set()
	square = SquareLocation(0,0)
	while square != next_square:
		tile = get_current_tile(square, solution_matrix, indexes)
		tile_ids.add(tile.tile_id)
		square = get_next_square(square, solution_matrix)
	return tile_ids

def print_matrix_counts(solution_matrix):
	for row in solution_matrix:
		print('|', end='')
		for item in row:
			print(' %s |' % len(item), end='')
		print('')

def print_matrix_ids(solution_matrix):
	for row in solution_matrix:
		print('|', end='')
		for item in row:
			print(' %s |' % item[-1].tile_id, end='')
		print('')
