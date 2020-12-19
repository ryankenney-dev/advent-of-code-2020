import re

def to_regex(rules):
	return '^%s$' % to_regex_inner(rules, 0)

def to_regex_inner(rules, rule_id):
	rule = rules[rule_id]
	if isinstance(rule, str):
		return rule
	return rule_tree_to_regex(rules, rule)

def rule_tree_to_regex(rules, rule_tree):
	if isinstance(rule_tree, int):
		return to_regex_inner(rules, rule_tree)
	elif 'or' in rule_tree:
		or_items = []
		for rule in rule_tree['or']:
			or_items.append(rule_tree_to_regex(rules, rule))
		return '(%s)' % '|'.join(or_items)
	elif 'seq' in rule_tree:
		sequence_str = ''
		for rule in rule_tree['seq']:
			sequence_str += rule_tree_to_regex(rules, rule)
		return sequence_str

rule_pattern = re.compile(r'^(\d+):\s(.+)$')
rule_string_pattern = re.compile(r'^"(\w+)"$')

def parse_input(input):
	rules = {}
	parts = input.split('\n\n')
	for line in parts[0].splitlines():
		match = rule_pattern.match(line)
		rule_id = int(match.group(1))
		rule_content = match.group(2)
		match = rule_string_pattern.match(rule_content)
		if match:
			rule = rules[rule_id] = match.group(1)
			continue
		or_parts = rule_content.split(' | ')
		if len(or_parts) > 1:
			rules[rule_id] = parse_or(or_parts)
			continue
		rules[rule_id] = parse_seq(rule_content)
	return { 'rules': rules, 'messages': parts[1].splitlines() }

def parse_or(or_parts):
	return { 
		'or': list(map(lambda s: parse_seq(s), or_parts))
	}


def parse_seq(sequence):
	sequence_parts = sequence.split(' ')
	return {
		'seq': list(map(lambda s: int(s), sequence_parts))
	}

def test_all_messages(input):
	parsed = parse_input(input)
	regex = re.compile(to_regex(parsed['rules']))
	result = []
	for line in parsed['messages']:
		result.append((bool(regex.match(line)), line))
	return result
