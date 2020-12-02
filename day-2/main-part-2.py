import re

def main(file_name):
    lines = None
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    
    entries = set()
    for line in lines:
        entries.add(line)
    
    valid_password_count = 0
    for entry in entries:
        match = re.match(r'^(\d+)-(\d+)\s+(\w):\s+(\w+)$', entry)
        first_char_pos = int(match.group(1))
        second_char_pos = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
   
        if ( password[first_char_pos-1] == char and password[second_char_pos-1] != char ) or ( password[first_char_pos-1] != char and password[second_char_pos-1] == char ):
            valid_password_count = valid_password_count + 1
            state_title = 'VALID '
        else:
            state_title = 'INVALID'
        print('%s %s or %s of %s in %s' % (state_title, first_char_pos, second_char_pos, char, password))
    
    print('Valid Password Count: %s' % valid_password_count)

#main('test-input')
main('input')

