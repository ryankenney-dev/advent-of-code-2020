import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

tiles = part_2.parse_input(message)
tiles_matrix = part_2.find_assembled_tiles(tiles)
uber_tile = part_2.join_tiles(tiles_matrix)
uber_tile = part_2.join_tiles(tiles_matrix)
dragon = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
found = part_2.find_image_in_all_tile_translations(uber_tile, dragon)
tile = found[0][0]
for coords in found[0][1]:
    tile = part_2.tile_apply_image(tile, dragon, coords)
print(part_2.tile_to_string(tile))
hash_count = part_2.tile_count_char(tile, '#')

print("")
print("[[[ '#' Count: %s ]]]" % hash_count)
print("")
