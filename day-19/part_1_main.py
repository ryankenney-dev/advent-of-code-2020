import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

result = part_1.test_all_messages(message)

count = sum(list(map(lambda i: i[0],result)))

print("")
print("[[[ Valid Messages: %s ]]]" % count)
print("")
