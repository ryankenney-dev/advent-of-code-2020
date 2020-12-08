import part_1
import json

test_cases = [{
	'input': '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''',
	'expected_contained_by_index': {
		'bright white': {'dark orange', 'light red'},
		'muted yellow': {'dark orange', 'light red'},
		'shiny gold': {'bright white', 'muted yellow'},
		'faded blue': {'dark olive', 'muted yellow', 'vibrant plum'},
		'dark olive': {'shiny gold'},
		'vibrant plum': {'shiny gold'},
		'dotted black': {'dark olive', 'vibrant plum'}
	},
	'bag_to_carry': 'shiny gold',
	'expected_possible_containers': {
		'bright white',
		'muted yellow',
		'dark orange',
		'light red'
	}
}]

for test_case in test_cases:
	dependencies = part_1.parse_message_to_contained_by_index(test_case['input'])
	#print(dependencies)
	if dependencies != test_case['expected_contained_by_index']:
		raise Exception('Unexpected')
	possible_containers = part_1.find_all_possible_containers(test_case['bag_to_carry'], dependencies)
	print(possible_containers)
	if possible_containers != test_case['expected_possible_containers']:
		raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
