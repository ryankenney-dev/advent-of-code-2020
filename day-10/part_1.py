
def parse_jolt_adapters(message):
    return list(map(lambda x: int(x), message.splitlines()))

def count_jolt_differences(jolt_adapters):
    jolt_adapters = jolt_adapters.copy()
    # Add the final jump to the devices power supply
    jolt_adapters.append(max(jolt_adapters) + 3)
    jolt_adapters.sort()
    previous_adapter = 0
    differences = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0
    }
    for adapter in jolt_adapters:
        difference = adapter - previous_adapter
        differences[str(difference)] = differences[str(difference)] + 1
        previous_adapter = adapter
    return differences

def product_of_1_and_3_jolt_differences(jolt_adapters):
    differences = count_jolt_differences(jolt_adapters)
    return differences['1'] * differences['3']
