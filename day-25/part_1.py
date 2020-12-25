
def parse_input(message):
    return list(map(lambda x: int(x), message.splitlines()))

def transform_subject_number(subject_number, loop_size):
    value = 1
    for i in range(0, loop_size):
        value = transform_subject_number_once(subject_number, value)
    return value

def transform_subject_number_once(subject_number, value):
    value *= subject_number
    value = value % 20201227
    return value

def find_loop_size(subject_number, public_key):
    value = 1
    loop_count = 0
    while True:
        value = transform_subject_number_once(subject_number, value)
        loop_count += 1
        if public_key == value:
            return loop_count

def find_encryption_key(public_keys, subject_number):
    loop_sizes = []
    for public_key in public_keys:
        loop_size = find_loop_size(7, public_key)
        loop_sizes.append(loop_size)
    return transform_subject_number(public_keys[0], loop_sizes[1])
