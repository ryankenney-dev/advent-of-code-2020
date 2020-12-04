import re

required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def passport_has_required_fields(passport):
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True

def read_file_to_messages(file_path):
    with open(file_path, 'r') as f:
        return f.read().split('\n\n')

def process_messages(messages):
    total_passport_count = 0
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
    
        valid_passport = passport_has_required_fields(passport)
        if valid_passport:
            valid_passport_count = valid_passport_count + 1
        total_passport_count = total_passport_count + 1
        print("[valid=%s] %s" % (valid_passport, passport))

    return {
            'valid_count': valid_passport_count,
            'invalid_count': total_passport_count - valid_passport_count,
            'empty_entry_count': empty_entry_count
        }

