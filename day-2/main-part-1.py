import re

def count_char_in(char, string):
    count = 0
    for c in string: 
        if c == char: 
            count = count + 1
    return count

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
        print('%s to %s of %s in %s' % (match.group(1),match.group(2),match.group(3),match.group(4)))
        min_count = int(match.group(1))
        max_count = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
    
        count = count_char_in(char, password)
    
        if count >= min_count and count <= max_count:
            valid_password_count = valid_password_count + 1
    
    print('Valid Password Count: %s' % valid_password_count)

#main('test-input')
main('input')
