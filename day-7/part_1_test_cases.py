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
	'expected_dependencies': {
		'light red': [
			{
				'count': '1',
				'color': 'bright white'
			},
			{
				'count': '2',
				'color': 'muted yellow'
			}
		],
		'dark orange': [
			{
				'count': '3',
				'color': 'bright white'
			},
			{
				'count': '4',
				'color': 'muted yellow'
			}
		],
		'bright white': [
			{
				'count': '1',
				'color': 'shiny gold'
			}
		],
		'muted yellow': [
			{
				'count': '2',
				'color': 'shiny gold'
			},
			{
				'count': '9',
				'color': 'faded blue'
			}
		],
		'shiny gold': [
			{
				'count': '1',
				'color': 'dark olive'
			},
			{
				'count': '2',
				'color': 'vibrant plum'
			}
		],
		'dark olive': [
			{
				'count': '3',
				'color': 'faded blue'
			},
			{
				'count': '4',
				'color': 'dotted black'
			}
		],
		'vibrant plum': [
			{
				'count': '5',
				'color': 'faded blue'
			},
			{
				'count': '6',
				'color': 'dotted black'
			}
		],
		'faded blue': [],
		'dotted black': []
	}
}]

for test_case in test_cases:
	#print(json.dumps(part_1.parse_message_to_dependencies(test_case['input']), indent=4))
	dependencies = part_1.parse_message_to_dependencies(test_case['input'])
	if dependencies != test_case['expected_dependencies']:
		raise Exception('Unexpected')

print("")
print("[[[ SUCCESS ]]]")
print("")
