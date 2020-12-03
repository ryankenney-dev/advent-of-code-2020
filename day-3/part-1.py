
lines = None
with open('input', 'r') as f:
    lines = f.read().splitlines()

coord_down = 0
coord_right = 0
tree_count = 0
while coord_down < len(lines):
    char = lines[coord_down][coord_right % len(lines[coord_down])]
    if char == '#':
        tree_count = tree_count + 1
    coord_down = coord_down + 1
    coord_right = coord_right + 3

print("Hit Trees: %s" % tree_count)

