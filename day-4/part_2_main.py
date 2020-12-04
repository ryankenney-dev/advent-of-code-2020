import part_2, sys, json

messages = part_2.read_file_to_messages(sys.argv[1])
result = part_2.process_messages(messages)

print("----")
print(json.dumps(result, indent=4, sort_keys=True))
