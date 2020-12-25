import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

public_keys = part_1.parse_input(message)
encryption_key = part_1.find_encryption_key(public_keys, 7)

print("")
print("[[[ Result: %s ]]]" % encryption_key)
print("")
