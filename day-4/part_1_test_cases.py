import part_1

messages = part_1.read_file_to_messages('input_provided-part-1')
result = part_1.process_messages(messages)

if result['invalid_count'] != 2:
    raise Exception('Invalid counts: %s' % result)
if result['valid_count'] != 2:
    raise Exception('Invalid counts: %s' % result)

print("")
print("[[[ SUCCESS ]]]")
