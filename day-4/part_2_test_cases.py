import part_2

base_message = 'byr:2000 pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 hcl:#623a2f'


test_cases = [{
    'expected_valid': True, 'message': base_message + ' byr:1920'
},{
    'expected_valid': True, 'message': base_message + ' byr:2002'
},{
    'expected_valid': True, 'message': base_message + ' iyr:2010'
},{
    'expected_valid': True, 'message': base_message + ' iyr:2020'
},{
    'expected_valid': True, 'message': base_message + ' eyr:2020'
},{
    'expected_valid': True, 'message': base_message + ' eyr:2030'
},{
    'expected_valid': True, 'message': base_message + ' hgt:150cm'
},{
    'expected_valid': True, 'message': base_message + ' hgt:193cm'
},{
    'expected_valid': True, 'message': base_message + ' hgt:59in'
},{
    'expected_valid': True, 'message': base_message + ' hgt:76in'
},{
    'expected_valid': True, 'message': base_message + ' hcl:#123456'
},{
    'expected_valid': True, 'message': base_message + ' hcl:#abcdef'
},{
    'expected_valid': True, 'message': base_message + ' ecl:brn'
},{
    'expected_valid': True, 'message': base_message + ' ecl:blu'
},{
    'expected_valid': True, 'message': base_message + ' pid:123456789'
},{
    'expected_valid': True, 'message': base_message + ' pid:000000001'
},{
    'expected_valid': False, 'message': base_message + 'byr:1919'
},{
    'expected_valid': False, 'message': base_message + 'byr:2003'
},{
    'expected_valid': False, 'message': base_message + 'byr:200'
},{
    'expected_valid': False, 'message': base_message + 'byr:20000'
},{
    'expected_valid': False, 'message': base_message + 'byr:a'
},{
    'expected_valid': False, 'message': base_message + 'iyr:2009'
},{
    'expected_valid': False, 'message': base_message + 'iyr:2021'
},{
    'expected_valid': False, 'message': base_message + 'iyr:200'
},{
    'expected_valid': False, 'message': base_message + 'iyr:20000'
},{
    'expected_valid': False, 'message': base_message + 'iyr:a'
},{
    'expected_valid': False, 'message': base_message + 'eyr:2019'
},{
    'expected_valid': False, 'message': base_message + 'eyr:2031'
},{
    'expected_valid': False, 'message': base_message + 'eyr:200'
},{
    'expected_valid': False, 'message': base_message + 'eyr:20000'
},{
    'expected_valid': False, 'message': base_message + 'eyr:a'
},{
    'expected_valid': False, 'message': base_message + 'hgt:149cm'
},{
    'expected_valid': False, 'message': base_message + 'hgt:194cm'
},{
    'expected_valid': False, 'message': base_message + 'hgt:58in'
},{
    'expected_valid': False, 'message': base_message + 'hgt:77in'
},{
    'expected_valid': False, 'message': base_message + 'hgt:150xx'
},{
    'expected_valid': False, 'message': base_message + 'hgt:80xx'
},{
    'expected_valid': False, 'message': base_message + 'hcl:#12345'
},{
    'expected_valid': False, 'message': base_message + 'hcl:#1234567'
},{
    'expected_valid': False, 'message': base_message + 'hcl:#12345z'
},{
    'expected_valid': False, 'message': base_message + 'hcl:123456'
},{
    'expected_valid': False, 'message': base_message + 'ecl:wat'
},{
    'expected_valid': False, 'message': base_message + 'ecl:BRN'
},{
    'expected_valid': False, 'message': base_message + 'pid:12345678'
},{
    'expected_valid': False, 'message': base_message + 'pid:1234567890'
},{
    'expected_valid': False, 'message': base_message + 'pid:0123456789'
}]


for test_case in test_cases:
    result = part_2.process_messages([test_case['message']])
    if test_case['expected_valid']:
        expected_valid_count = 1
    else:
        expected_valid_count = 0
    if expected_valid_count != result['valid_count']:
        raise Exception('Invalid result for test case: %s' % test_case['message'])

print("")
print("[[[ SUCCESS ]]]")
