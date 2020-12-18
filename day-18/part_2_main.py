import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

expressions = message.splitlines()
total_sum = 0
for expression in expressions:
	expr_tree = part_2.parse_into_exp_tree(expression)
	total_sum += part_2.compute(expr_tree)

print("")
print("[[[ Result: %s ]]]" % total_sum)
print("")
