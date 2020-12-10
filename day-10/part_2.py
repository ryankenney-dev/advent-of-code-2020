
def parse_jolt_adapters(message):
    return list(map(lambda x: int(x), message.splitlines()))

def find_all_combinations(jolt_adapters):
    jolt_adapters = jolt_adapters.copy()
    # Add the first jump from 0
    jolt_adapters.append(0)
    # Add the final jump to the devices power supply
    jolt_adapters.append(max(jolt_adapters) + 3)
    jolt_adapters.sort()
    return find_all_combinations_inner(jolt_adapters, 0)

def find_all_combinations_inner(jolt_adapters, current_index):
    current_adapter = jolt_adapters[current_index]
    if current_index == len(jolt_adapters)-1:
        return [[current_adapter]]
    combinations = []
    for i in range(current_index+1, len(jolt_adapters)):
        if jolt_adapters[i] - current_adapter > 3:
            break
        nested_combinations = find_all_combinations_inner(jolt_adapters, i)
        for nested_combination in nested_combinations:
            nested_combination.insert(0, current_adapter)
        combinations.extend(nested_combinations)
    return combinations

def count_all_combinations(jolt_adapters):
    jolt_adapters = jolt_adapters.copy()
    # Add the first jump from 0
    jolt_adapters.append(0)
    # Add the final jump to the devices power supply
    jolt_adapters.append(max(jolt_adapters) + 3)
    jolt_adapters.sort()
    return count_all_combinations_inner(jolt_adapters, 0, {})

def count_all_combinations_inner(jolt_adapters, current_index, solutions_cache):
    current_adapter = jolt_adapters[current_index]
    if current_index == len(jolt_adapters)-1:
        return 1
    combinations = 0
    for i in range(current_index+1, len(jolt_adapters)):
        nested_adapter = jolt_adapters[i]
        if nested_adapter - current_adapter > 3:
            break
        # NOTE: The solutions_cache containers solutions for subtress that
        # have already been visited
        if str(nested_adapter) in solutions_cache:
            nested_count = solutions_cache[str(nested_adapter)]
        else:
            nested_count = count_all_combinations_inner(jolt_adapters, i, solutions_cache)
            solutions_cache[str(nested_adapter)] = nested_count
        combinations = combinations + nested_count
    return combinations
