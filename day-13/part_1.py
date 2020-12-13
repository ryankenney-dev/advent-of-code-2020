from collections import namedtuple

Notes = namedtuple('Notes', ['earliest_time', 'buses'])

def parse_message_to_notes(message):
    lines = message.splitlines()
    return Notes(earliest_time = int(lines[0]), \
        buses = list(map(lambda b: int(b), filter(lambda b: b != 'x', lines[1].split(',')))))

WaitEntry = namedtuple('WaitEntry', ['bus', 'wait_time'])

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
