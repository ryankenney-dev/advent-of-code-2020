import part_2
import sys

index = None
with open(sys.argv[1], 'r') as f:
    index = part_2.parse_message_to_contains_index(f.read())

count = part_2.count_all_nested_contents('shiny gold', index)

print("")
print("[[[ Count of nested bags: %s ]]]" % count)
print("")
