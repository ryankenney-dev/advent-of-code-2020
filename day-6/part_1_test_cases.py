import part_1
import sys

test_cases = [{
	'input': '''abc

a
b
c

ab
ac

a
a
a
a

b''',
	'expected_question_sets': [
		('a','b','c'),
		('a','b','c'),
		('a','b','c'),
		('a'),
		('b')
	],
	'expected_sum': 11
}]

for test_case in test_cases:
	family_responses = part_1.read_input_to_family_responses(test_case['input'])
	for i in range(0, len(family_responses)):
		question_ids = part_1.family_responses_to_question_ids(family_responses[i])
		expected_question_ids = test_case['expected_question_sets'][i]
		for expected_question_id in expected_question_ids:
			if expected_question_id not in question_ids:
				raise Exception('Expected set %s does not match %s for index %s' % (expected_question_ids, question_ids, i))
		if len(question_ids) != len(expected_question_ids):
			raise Exception('Expected set %s does not match %s for index %s' % (expected_question_ids, question_ids, i))

	sum = part_1.family_responses_to_sum_of_responses(family_responses)
	if test_case['expected_sum'] != sum:
		raise Exception('Expected sum %s does not match %s' % (test_case['expected_sum'], sum))

print("")
print("[[[ SUCCESS ]]]")
print("")
