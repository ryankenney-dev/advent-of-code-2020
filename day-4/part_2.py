import re

required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def passport_has_required_fields(passport):
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True

def year_field_is_valid(value, min_year, max_year):
    if not re.match(r'\d{4}', value):
        return False
    int_value = int(value)
    if int_value < min_year or int_value > max_year:
        return False
    return True

def passport_fields_are_valid(passport):
    if not year_field_is_valid(passport['byr'], 1920, 2002):
        return False
    if not year_field_is_valid(passport['iyr'], 2010, 2020):
        return False
    if not year_field_is_valid(passport['eyr'], 2020, 2030):
        return False
    match = re.match(r'(^\d+)(cm|in)$', passport['hgt'])
    if not match:
        return False
    if match.group(2) == 'cm':
        height = int(match.group(1))
        if height < 150 or height > 193:
            return False
    elif match.group(2) == 'in':
        height = int(match.group(1))
        if height < 59 or height > 76:
            return False
    else:
        return False
    match = re.match(r'^#[a-f0-9]{6}$', passport['hcl'])
    if not match:
        return False
    match = re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', passport['ecl'])
    if not match:
        return False
    match = re.match(r'^\d{9}$', passport['pid'])
    if not match:
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
    
        valid_passport = False
        if passport_has_required_fields(passport):
            if passport_fields_are_valid(passport):
                valid_passport = True
    
        if valid_passport:
            valid_passport_count = valid_passport_count + 1
        total_passport_count = total_passport_count + 1
        print("[valid=%s] %s" % (valid_passport, passport))

    return {
            'valid_count': valid_passport_count,
            'invalid_count': total_passport_count - valid_passport_count,
            'empty_entry_count': empty_entry_count
        }

