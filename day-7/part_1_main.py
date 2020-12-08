import part_1
import sys

index = None
with open(sys.argv[1], 'r') as f:
    index = part_1.parse_message_to_contained_by_index(f.read())

possible_containers = part_1.find_all_possible_containers('shiny gold', index)

print("")
print("[[[ Count of possible containers: %s ]]]" % len(possible_containers))
print("")
