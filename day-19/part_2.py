import re
import copy

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
	result = []
	for line in parsed['messages']:
		result.append((match_string(line, parsed['rules']), line))
	return result

def match_string(s, rules):
	initial_thread = { 'seq_stack': [{ 'rule_id': 0, 'or_idx': 0, 'seq_idx': 0 }] }
	threads = [initial_thread]
	for char_idx in range(0, len(s)):
		char = s[char_idx]

		# print('-- char %s:%s --' % (char_idx, char))

		threads = match_char(char, char_idx, rules, threads)
		if len(threads) < 1:
			return False

	for thread in threads:
		# If the stack isn't empty, there are unmatched trailing rules
		if len(thread['seq_stack']) == 0:
			return True

	return False

EXAMPLE = {
	'seq_stack': [
		{ 'rule_id': 0, 'or_idx': 0, 'seq_idx': 0 },
		{ 'rule_id': 0, 'or_idx': 0, 'seq_idx': 0 }
	]
}

def validate_solution_history(thread, rules):
	for solution in thread['solutions']:
		next_rule_id = 0
		for entry in solution['seq_stack']:
			if next_rule_id != entry['rule_id']:
				raise Exception('Invalid entry')
			rule = rules[next_rule_id]
			if 'or' in rule:
				next_rule_id = rule['or'][entry['or_idx']]['seq'][entry['seq_idx']]
			elif 'seq' in rule:
				next_rule_id = rule['seq'][entry['seq_idx']]
			else:
				raise Exception('Invalid entry')
		if solution['char'] != rules[next_rule_id]:
			raise Exception('Char not matched')

# Theory of operation:
# * Maintain state as a stack of sequences
# * On "or", clone the entire state (called a thread)
#   and in clone (fork) apply a different or clause
# * Evaluate until all threads match/don't match this char
def match_char(char, char_idx, rules, unsolved_threads):
	solved_threads = []
	while len(unsolved_threads) > 0:
		thread = unsolved_threads.pop()

		# print('Thread: %s' % thread)

		if len(thread['seq_stack']) < 1:
			# We ran out of rules
			continue

		last_state = thread['seq_stack'][-1]
		last_rule_id = last_state['rule_id']
		last_rule = rules[last_rule_id]
		last_seq_idx = last_state['seq_idx']
		last_or_idx = last_state['or_idx']
		if 'or' in last_rule:
			rule_id = last_rule['or'][last_or_idx]['seq'][last_seq_idx]
		elif 'seq' in last_rule:
			rule_id = last_rule['seq'][last_seq_idx]
		else:
			raise Exception('Invalid entry: %s' % last_rule)

		rule = rules[rule_id]

		# print('Rule: %s' % rule)

		# If we hit these rules twice without advancing
		# to a new char, we're in an infinite loop.
		if rule_id == 8:
			if 'last_rule_8_char_idx' in thread:
				if thread['last_rule_8_char_idx'] == char_idx:
					continue
			thread['last_rule_8_char_idx'] = char_idx
		if rule_id == 11:
			if 'last_rule_11_char_idx' in thread:
				if thread['last_rule_11_char_idx'] == char_idx:
					continue
			thread['last_rule_11_char_idx'] = char_idx

		if isinstance(rule, str):
			# Not a match
			if char != rule:

				# print('Not a match: %s %s' % (char, rule))

				continue

			# print('Marking thread solved: %s' % thread)

			save_solution_history(thread, char)

			# Walk to next element in parent sequence (for next chat match)
			increment_seq_stack(thread, rules)

			solved_threads.append(thread)

		elif 'seq' in rule:
			thread['seq_stack'].append({ 'rule_id': rule_id, 'or_idx': 0, 'seq_idx': 0 })
			unsolved_threads.append(thread)

		elif 'or' in rule:
			# Duplicate (fork) thread for each or clause
			forked_threads = []
			for term_idx in range(0,len(rule['or'])):
				# NOTE: Ok ok... making one extra copy that we toss out,
				# but keeps logic simple
				forked_thread = copy.deepcopy(thread)
				forked_threads.append(forked_thread)
				# Put the or'd clause at the top of the stack
				forked_thread['seq_stack'].append({ 'rule_id': rule_id, 'or_idx': term_idx , 'seq_idx': 0 })

			# print('forked: %s', len(forked_threads))

			unsolved_threads.extend(forked_threads)

	return solved_threads

def increment_seq_stack(thread, rules):

	# print('Incn seq stack (before): %s' % thread)

	# Pop off all parent sequences we've exhausted
	while len(thread['seq_stack']) > 0 and \
		top_of_stack_exhausted(thread['seq_stack'], rules):

		# print('Popped stack of: %s' % thread['seq_stack'][-1])

		thread['seq_stack'].pop()
	# Increment resulting top sequence
	if len(thread['seq_stack']) > 0:
		thread['seq_stack'][-1]['seq_idx'] += 1
	# If no stack entries remain (and another char is encounterd),
	# it'll be detected on the next cycle above.

	# print('Incn seq stack (after): %s' % thread)


def top_of_stack_exhausted(stack, rules):
	top = stack[-1]
	rule = rules[top['rule_id']]
	if 'seq' in rule:
		seq = rule['seq']
	elif 'or' in rule:
		seq = rule['or'][top['or_idx']]['seq']
	else:
		raise Exception('Invalid entry: %s' % rule)
	return top['seq_idx']+1 >= len(seq)


USE_SOLUTION_HISTORY=False

def save_solution_history(thread, char):
	if not USE_SOLUTION_HISTORY:
		return
	if 'solutions' not in thread:
		thread['solutions'] = []
	thread['solutions'].append({ 'char':char, 'seq_stack':copy.deepcopy(thread['seq_stack']) })
