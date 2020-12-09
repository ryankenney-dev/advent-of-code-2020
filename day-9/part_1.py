
def find_first_invalid_value(lines, preamble_size):
    # For each line, after initial preamble
    for l in range(preamble_size, len(lines)):
        sum_value = int(lines[l])
        # NOTE: Plenty of efficiency to be gained by sorting and comparing
        preamble = set(lines[l-preamble_size:l])
        found_compliment = False
        for first_value in preamble:
            compliment_value = sum_value - int(first_value)
            if str(compliment_value) in preamble:
                found_compliment = True
                break
        if not found_compliment:
            return sum_value
    return -1

def find_contiguous_range_adding_to(lines, target_value):
    for i in range(0,len(lines)):
        current_sum = 0
        for j in range(i,len(lines)):
            current_sum = current_sum + int(lines[j])
            # j>1 ensures at least two entries in range
            if current_sum == target_value and j>1:
                return lines[i:j+1]
            if current_sum > target_value:
                break
    raise Exception('Not found')

def find_sum_of_min_max_of_contiguous_range_adding_to(lines, target_value):
    lines = find_contiguous_range_adding_to(lines, target_value)
    values = []
    for line in lines:
        values.append(int(line))
    return min(values) + max(values)
