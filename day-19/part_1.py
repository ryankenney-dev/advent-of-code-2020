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
	initial_thread = { 'seq_stack': [{ 'idx': 0, 'seq': [0] }] }
	threads = [initial_thread]
	for char in s:
		threads = match_char(char, rules, threads)
		if len(threads) < 1:
			return False
	return True

# Theory of operation:
# * Maintain state as a stack of sequences
# * On "or", clone the entire state (called a thread)
#   and in clone (fork) apply a different or clause
# * Evaluate until all threads match/don't match this char
def match_char(char, rules, unsolved_threads):
	solved_threads = []
	while len(unsolved_threads) > 0:
		thread = unsolved_threads.pop()

		# print('Thread: %s' % thread)

		if len(thread['seq_stack']) < 1:
			# We ran out of rules
			continue

		state = thread['seq_stack'][-1]
		rule_id = state['seq'][state['idx']]
		rule = rules[rule_id]

		# print('Rule: %s' % rule)

		if isinstance(rule, str):
			# Not a match
			if char != rule:

				# print('Not a match: %s %s' % (char, rule))

				continue
			# Walk to next element in parent sequence (for next chat match)
			increment_seq_stack(thread)

			# print('Marking thread solved: %s' % thread)

			solved_threads.append(thread)

		elif 'seq' in rule:
			thread['seq_stack'].append({ 'idx': 0, 'seq': rule['seq'] })
			unsolved_threads.append(thread)

		elif 'or' in rule:
			# Duplicate (fork) thread for each or clause
			forked_threads = []
			for term in rule['or']:
				# NOTE: Ok ok... making one extra copy that we toss out,
				# but keeps logic simple
				forked_thread = copy.deepcopy(thread)
				forked_threads.append(forked_thread)
				# Put the or'd clause at the top of the stack
				forked_thread['seq_stack'].append({ 'idx': 0, 'seq': term['seq'] })

			# print('forked: %s', len(forked_threads))

			unsolved_threads.extend(forked_threads)

	return solved_threads

def increment_seq_stack(thread):

	# print('Incn seq stack (before): %s' % thread)

	# Pop off all parent sequences we've exhausted
	while len(thread['seq_stack']) > 0 and \
		thread['seq_stack'][-1]['idx']+1 >= len(thread['seq_stack'][-1]['seq']):

		# print('Popped stack of: %s' % thread['seq_stack'][-1])

		thread['seq_stack'].pop()
	# Increment resulting top sequence
	if len(thread['seq_stack']) > 0:
		thread['seq_stack'][-1]['idx'] += 1
	# If no stack entries remain (and another char is encounterd),
	# it'll be detected on the next cycle above.

	# print('Incn seq stack (after): %s' % thread)
