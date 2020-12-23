
def parse_input(input):
	return list(map(lambda x: int(x), list(input)))

def run_cycle(cups):

	# "Before the crab starts, it will designate the first cup in your
	# list as the current cup."
	current_cup = cups[0]
	# "The crab picks up the three cups that are immediately clockwise of
	# the current cup."
	picked_up_cups = cups[1:4]
	# "They are removed from the circle"
	cups = cups[0:1] + cups[4:]

	# "The crab selects a destination cup: the cup with a label equal to
	# the current cup's label minus one. If this would select one of the
	# cups that was just picked up, the crab will keep subtracting one
	# until it finds a cup that wasn't just picked up. If at any point
	# in this process the value goes below the lowest value on any cup's label,
	# it wraps around to the highest value on any cup's label instead."
	smaller_cups = list(filter(lambda c: c < current_cup, cups.copy()))
	if len(smaller_cups) > 0:
		destination_cup = max(smaller_cups)
	else:
		destination_cup = max(cups)
	destination_idx = cups.index(destination_cup)

	# "The crab places the cups it just picked up so that they are
	# immediately clockwise of the destination cup. They keep the same
	# order as when they were picked up."
	cups = cups[0:destination_idx+1] + picked_up_cups + cups[destination_idx+1:]

	# "The crab selects a new current cup: the cup which is immediately
	# clockwise of the current cup."
	# (current is first index)
	new_current_idx = (cups.index(current_cup) + 1) % len(cups)
	cups = cups[new_current_idx:] + cups[0:new_current_idx]

	return cups

def get_cycle_signature(cups):
	# "Starting after the cup labeled 1, collect the other cups'
	# labels clockwise into a single string with no extra characters"
	one_index = cups.index(1)
	cups = cups[one_index+1:] + cups[0:one_index]

	return ''.join(list(map(lambda c: str(c), cups)))