import re

required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

message = None
with open('input', 'r') as f:
    messages = f.read().split('\n\n')

valid_passport_count = 0
empty_entry_count = 0
for message in messages:
    #print("Message : %s" % message)
    passport = {}
    for entry in re.split(r'\s+', message):
        #print("Entry : '%s'" % entry)
        if entry == '':
            # No idea why I'm getting an empty string at the end
            print('Empty entry!')
            empty_entry_count = empty_entry_count + 1
            continue

        match = re.match(r'^(\w\w\w):(.+)$', entry)
        passport[match.group(1)] = match.group(2)

    valid_passport = True
    for field in required_fields:
        if field not in passport.keys():
            valid_passport = False
            break

    if valid_passport:
        valid_passport_count = valid_passport_count + 1
    print("[valid=%s] %s" % (valid_passport, passport))

print("----")
print("Valid count: %s" % valid_passport_count)
print("Empty entry count: %s" % empty_entry_count)
