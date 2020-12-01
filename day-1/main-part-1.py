

lines = None
with open('input', 'r') as f:
    lines = f.read().splitlines()

entries = set()
for line in lines:
    print(line)
    entries.add(int(line))

target_entry = None
for entry in entries:
    if (2020 - entry) in entries:
        target_entry = entry
        break

if target_entry is None:
    raise Exception("Not found!")

result = target_entry * (2020 - target_entry)

print("Result: %s" % result)
