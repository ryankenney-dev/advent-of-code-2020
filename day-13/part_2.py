from collections import namedtuple

Notes = namedtuple('Notes', ['earliest_time', 'buses'])

Bus = namedtuple('Bus', ['interval', 'offset'])

def parse_to_buses(message):
    lines = message.splitlines()

    buses = []
    bus_index = 0
    for bus in lines[1].split(','):
        if bus != 'x':
            buses.append(Bus(int(bus), bus_index))
        bus_index += 1
    return buses

WaitEntry = namedtuple('WaitEntry', ['bus', 'wait_time'])

# Theory of solution:
#
# * First walk in increments of the first bus' interval
#   to find a solution for the first two buses
# * After finding a solution for the first pair, continuing
#   walking increments of the first bus to find a second
#   solution to the pair of buses. The difference between these
#   solutions is the same of all futher solutions for these
#   two buses.
# * Repeat the process for each successive bus, using the previously
#   calculated difference between two solutions as the incrementor.
#
def find_time_with_bus_offsets(buses):
    # Sort buses by offset
    buses = buses.copy()
    buses.sort(key=lambda x: x.offset)

    # Jumps between solutions per buses already solved for
    time_increment = buses[0].interval
    # The last witnessed solution
    last_solution_time = 0

    for b in range(1, len(buses)):
        bus = buses[b]
        solutions = []
        time_increment_count = 0
        while True:
            timestamp = last_solution_time + time_increment * time_increment_count
            if bus_aligns_with_timestamp(bus, timestamp):
                solutions.append(timestamp)
                if len(solutions) > 1:
                    time_increment = solutions[1] - solutions[0]
                    last_solution_time = solutions[0]
                    break
            time_increment_count += 1
    return last_solution_time

def bus_aligns_with_timestamp(bus, timestamp):
    return (timestamp + bus.offset) % bus.interval == 0
