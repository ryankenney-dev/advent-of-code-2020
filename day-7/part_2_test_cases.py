import part_2
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
	'expected_contains_index': {
		'light red': [{'count': '1', 'color': 'bright white'}, {'count': '2', 'color': 'muted yellow'}],
		'dark orange': [{'count': '3', 'color': 'bright white'}, {'count': '4', 'color': 'muted yellow'}],
		'bright white': [{'count': '1', 'color': 'shiny gold'}],
		'muted yellow': [{'count': '2', 'color': 'shiny gold'}, {'count': '9', 'color': 'faded blue'}],
		'shiny gold': [{'count': '1', 'color': 'dark olive'}, {'count': '2', 'color': 'vibrant plum'}],
		'dark olive': [{'count': '3', 'color': 'faded blue'}, {'count': '4', 'color': 'dotted black'}],
		'vibrant plum': [{'count': '5', 'color': 'faded blue'}, {'count': '6', 'color': 'dotted black'}],
		'faded blue': [], 'dotted black': []
	},
	'bag_to_carry': 'shiny gold',
	'expected_contained_count': 32
},{
	'input': '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.''',
	'expected_contains_index': {
		'shiny gold': [{'count': '2', 'color': 'dark red'}],
		'dark red': [{'count': '2', 'color': 'dark orange'}],
		'dark orange': [{'count': '2', 'color': 'dark yellow'}],
		'dark yellow': [{'count': '2', 'color': 'dark green'}],
		'dark green': [{'count': '2', 'color': 'dark blue'}],
		'dark blue': [{'count': '2', 'color': 'dark violet'}],
		'dark violet': []
	},
	'bag_to_carry': 'shiny gold',
	'expected_contained_count': 126
}]

for test_case in test_cases:
	index = part_2.parse_message_to_contains_index(test_case['input'])
	print(index)
	if index != test_case['expected_contains_index']:
		raise Exception('Unexpected')
	contained_count = part_2.count_all_nested_contents(test_case['bag_to_carry'], index)
	print(contained_count)
	if contained_count != test_case['expected_contained_count']:
		raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
