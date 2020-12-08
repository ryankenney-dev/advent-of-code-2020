import regex

bag_pattern = '(\\w+ \\w+) bags?'
line_pattern_no_other_bags = regex.compile('^%s contain no other bags.$' % bag_pattern)
line_pattern_other_bags = regex.compile('^%s contain(,? (\\d+) %s)+\\.$' % (bag_pattern, bag_pattern))

def parse_line_to_dependencies(line):
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

def parse_message_to_dependencies(message):
	result = []
	for line in message.splitlines():
		result.append(parse_line_to_dependencies(line))
	return result


