
lines = None
with open('input', 'r') as f:
    lines = f.read().splitlines()

def count_trees(right_inc, down_inc):
    coord_down = 0
    coord_right = 0
    tree_count = 0
    while coord_down < len(lines):
        char = lines[coord_down][coord_right % len(lines[coord_down])]
        if char == '#':
            tree_count = tree_count + 1
        coord_down = coord_down + down_inc 
        coord_right = coord_right + right_inc
    return tree_count

print("Hit Trees:")
print(count_trees(1, 1))
print(count_trees(3, 1))
print(count_trees(5, 1))
print(count_trees(7, 1))
print(count_trees(1, 2))

product = 1
product = product * count_trees(1, 1)
product = product * count_trees(3, 1)
product = product * count_trees(5, 1)
product = product * count_trees(7, 1)
product = product * count_trees(1, 2)

print("RESULT: %s" % product)
