

lines = None
with open('input', 'r') as f:
    lines = f.read().splitlines()

entries = set()
for line in lines:
    print(line)
    entries.add(int(line))

target_entries = None
for entry1 in entries:
    for entry2 in entries:
        if entry1 == entry2:
            continue
        if (2020 - entry1 - entry2) in entries:
            target_entries = (entry1, entry2, 2020 - entry1 - entry2)
            break

if target_entries is None:
    raise Exception("Not found!")

print("Entries: %s %s %s" % target_entries)

result = target_entries[0] * target_entries[1] * target_entries[2]

print("Result: %s" % result)
