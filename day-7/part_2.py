import regex

bag_pattern = '(\\w+ \\w+) bags?'
line_pattern_no_other_bags = regex.compile('^%s contain no other bags.$' % bag_pattern)
line_pattern_other_bags = regex.compile('^%s contain(,? (\\d+) %s)+\\.$' % (bag_pattern, bag_pattern))

def parse_line(line):
	match = line_pattern_no_other_bags.match(line)
	if match:
		return {
			'color': match.group(1),
			'contains': []
		}
	match = line_pattern_other_bags.match(line)
	if not match:
		raise Exception('Unrecognized format in line [%s]' % line)
	color = match.group(1)
	inner_counts = match.captures(3)
	inner_colors = match.captures(4)
	inner_bags = []
	for i in range(0, len(inner_counts)):
		inner_bags.append({
			'count': inner_counts[i],
			'color': inner_colors[i]
		})
	return {
		'color': color,
		'contains': inner_bags
	}

def parse_message_to_contained_by_index(message):
	index = {}
	for line in message.splitlines():
		parsed = parse_line(line)
		outer_bag = parsed['color']
		for inner_bag in parsed['contains']:
			inner_bag_color = inner_bag['color']
			if inner_bag_color not in index:
				index[inner_bag_color] = set()
			index[inner_bag_color].add(outer_bag)
	return index

def parse_message_to_contains_index(message):
	index = {}
	for line in message.splitlines():
		parsed = parse_line(line)
		outer_bag = parsed['color']
		index[outer_bag] = parsed['contains']
	return index

def find_all_possible_containers(color, dependencies_index):
	collected_containers = set();
	find_all_possible_containers_inner(color, dependencies_index, collected_containers)
	return collected_containers

def find_all_possible_containers_inner(color, dependencies_index, collected_containers):
	if color not in dependencies_index.keys():
		return
	containers = dependencies_index[color]
	for container in containers:
		collected_containers.add(container)
		find_all_possible_containers_inner(container, dependencies_index, collected_containers)

def count_all_nested_contents(color, contains_index):
	# Minus one to exclude the outer most bag
	return count_all_nested_contents_inner(1, color, contains_index, 1) - 1

def count_all_nested_contents_inner(count, color, contains_index, depth):
	print('%scount: %s color %s' % (' '*depth, count, color))
	
	if color not in contains_index.keys():
		return count
	inner_bags = contains_index[color]
	if len(inner_bags) == 0:
		return count
	contents_count = count
	for inner_bag in inner_bags:
		contents_count = contents_count + \
			count_all_nested_contents_inner(
				count * int(inner_bag['count']), inner_bag['color'], contains_index, depth+1)
	return contents_count