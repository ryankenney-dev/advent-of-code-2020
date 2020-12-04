import part_1, sys, json

messages = part_1.read_file_to_messages(sys.argv[1])
result = part_1.process_messages(messages)

print("----")
print(json.dumps(result, indent=4, sort_keys=True))
