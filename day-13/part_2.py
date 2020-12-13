from collections import namedtuple

Notes = namedtuple('Notes', ['earliest_time', 'buses'])

Bus = namedtuple('Bus', ['interval', 'offset'])

def parse_to_buses_sorted_by_interval(message):
    lines = message.splitlines()

    buses = []
    bus_index = 0
    for bus in lines[1].split(','):
        if bus != 'x':
            buses.append(Bus(int(bus), bus_index))
        bus_index += 1
    buses.sort(key=lambda x: x.interval, reverse=True)
    return buses

WaitEntry = namedtuple('WaitEntry', ['bus', 'wait_time'])

# Assumes buses sorted larges to smalles interval (for performance)
def find_time_with_bus_offsets(buses):
    initial_bus_multiplier = 1
    while True:
        timestamp = buses[0].interval * initial_bus_multiplier - buses[0].offset
        found = True
        for i in range(1, len(buses)):
            bus = buses[i]
            if (timestamp + bus.offset) % bus.interval != 0:
                found = False
                break
        if found:
            return timestamp
        initial_bus_multiplier += 1

def find_bus_with_minimum_wait(notes):
    min_wait = notes.earliest_time
    min_wait_buses = []
    for bus in notes.buses:
        wait_time = bus - (notes.earliest_time % bus)
        if wait_time < min_wait:
            min_wait = wait_time
            min_wait_buses = []
        if wait_time <= min_wait:
            min_wait_buses.append(WaitEntry(bus, wait_time))
    if len(min_wait_buses) > 1:
        raise Exception('More than one solution')
    return min_wait_buses[0]

def compute_result(notes):
    wait_entry = find_bus_with_minimum_wait(notes)
    return wait_entry.wait_time * wait_entry.bus
