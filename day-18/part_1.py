import re

def parse_into_exp_tree(expression):
	int_pattern = re.compile(r'^\d+$')
	op_pattern = re.compile(r'^[\+\*]$')
	expression = expression.replace('(', '( ')
	expression = expression.replace(')', ' )')
	terms = expression.split(' ')

	current_context = []
	context_stack = [current_context]

	for term in terms:
		if int_pattern.match(term):
			current_context.append(int(term))
		elif op_pattern.match(term):
			current_context.append(term)
		elif term == '(':
			new_context = []
			current_context.append(new_context)
			context_stack.append(new_context)
			current_context = new_context
		elif term == ')':
			context_stack.pop()
			current_context = context_stack[-1]
		else:
			raise Exception('Invalid term [%s]' % term)
	return current_context


OPERATOR = {
	'+': lambda v1, v2: v1+v2,
	'*': lambda v1, v2: v1*v2,
}

def compute(expression_tree):
	op = None
	cumulative_value = None
	for term in expression_tree:

		if term == '+' or term == '*':
			op = term
			continue
		elif isinstance(term, int):
			op_value = term
		elif isinstance(term, list):
			op_value = compute(term)
		else:
			raise Exception('Invalid term [%s]' % term)

		# If this is the first value in the series,
		# just save the value
		if cumulative_value == None:
			cumulative_value = op_value
			continue

		cumulative_value = OPERATOR[op](cumulative_value, op_value)

	return cumulative_value
