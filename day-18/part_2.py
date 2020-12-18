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
	evaluate_all_op_expressions(expression_tree, '+')
	evaluate_all_op_expressions(expression_tree, '*')
	return expression_tree[0]

def evaluate_all_op_expressions(expression_tree, op):

	while len(expression_tree) > 1:
		op_found = False
		for term_idx in range(0, len(expression_tree)):
			if expression_tree[term_idx] == op:
				op_found = True
				break

		if not op_found:
			return

		# Capture left/right values
		left_value = expression_tree[term_idx-1]
		if isinstance(left_value, list):
			left_value = compute(left_value)
		right_value = expression_tree[term_idx+1]
		if isinstance(right_value, list):
			right_value = compute(right_value)

		# Compute result
		result = OPERATOR[op](left_value, right_value)

		# Replace three term in the expression_tree with the result
		expression_tree[term_idx-1] = result
		expression_tree.pop(term_idx)
		expression_tree.pop(term_idx)
