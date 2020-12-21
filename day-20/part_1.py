import re
import copy

tile_id_regex = re.compile(r'^Tile (\d+):$')

EDGE_NORTH=0
EDGE_EAST=1
EDGE_SOUTH=2
EDGE_WEST=3

class Tile:

	def __init__(self, other_tile):
		self.tile_id = other_tile.tile_id
		self.edges = copy.deepcopy(other_tile.edges)

	def __init__(self, text):
		lines = text.splitlines()
		match = tile_id_regex.match(lines[0])
		self.tile_id = int(match.group(1))
		north = lines[1]
		south = lines[-1][::-1]
		west = []
		east = []
		for line in lines[1:]:
			east.append(line[-1])
			west.insert(0, line[0])
		east = ''.join(east)
		west = ''.join(west)
		self.edges = [north, east, south, west]

	def get_edge(self, direction):
		'''
		Returns the edge signature, in clockwise direction across it.
		'''
		return self.edges[direction]

	def rotate(self):
		'''
		Returns a copy of the Tile, but rotated 90 degrees clockwise.
		'''
		tile = copy.deepcopy(self)
		tile.edges.insert(0, tile.edges.pop())
		return tile

	def translate(self, translation):
		'''
		Returns a copy of the Tile, but flipped left-to-right,
		then rotated 90 degrees clockwise by the number of times
		specified in the translation object
		'''
		tile = copy.deepcopy(self)

		if 'flip' in translation:
			for i in range(0, translation['flip']):
				# Reverse each edge
				for i in range(0, len(tile.edges)):
					tile.edges[i] = tile.edges[i][::-1]
				# Update edge order
				east = tile.edges[EDGE_EAST]
				tile.edges[EDGE_EAST] = tile.edges[EDGE_WEST]
				tile.edges[EDGE_WEST] = east

		if 'rotate' in translation:
			for i in range(0, translation['rotate']):
				tile.edges.insert(0, tile.edges.pop())

		return tile

def parse_input(message):
	tile_parts = message.split('\n\n')
	return list(map(lambda t: Tile(t), tile_parts))

standard_translations = [
	{'rotate': 0},
	{'rotate': 1},
	{'rotate': 2},
	{'rotate': 3},
	{'flip': 1, 'rotate': 0},
	{'flip': 1, 'rotate': 1},
	{'flip': 1, 'rotate': 2},
	{'flip': 1, 'rotate': 3},
]

def index_all_west_tile_edges(tiles):
	west_edge_signatures = {}
	for tile in tiles:
		for translation in standard_translations:
			translated = tile.translate(translation)
			west_edge = translated.get_edge(EDGE_WEST)
			if west_edge not in west_edge_signatures:
				west_edge_signatures[west_edge] = []
			west_edge_signatures[west_edge].append((tile.tile_id, translation))
	return west_edge_signatures
