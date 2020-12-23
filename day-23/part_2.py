import collections

class Game:

	def __init__(self, input, total_cup_count):
		index = [None] * total_cup_count
		initial_labels = list(map(lambda x: int(x), list(input)))
		first_cup = { 'label': initial_labels[0], 'next_cup': None }
		index[initial_labels[0]-1] = first_cup
		previous_cup = first_cup
		for label in initial_labels[1:]:
			cup = { 'label': label, 'next_cup': None }
			index[label-1] = cup
			self.set_next(previous_cup, cup)
			previous_cup = cup
		for i in range(len(initial_labels), total_cup_count):
			label = i+1
			cup = { 'label': label, 'next_cup': None }
			index[label-1] = cup
			self.set_next(previous_cup, cup)
			previous_cup = cup
		self.set_next(previous_cup, first_cup)
		self.current_cup = first_cup
		self.index = index

	def run_cycle(self):

		# "The crab picks up the three cups that are immediately clockwise of
		# the current cup."
		# "They are removed from the circle"
		picked_up_cups = self.pickup_cups()

		# "The crab selects a destination cup: the cup with a label equal to
		# the current cup's label minus one. If this would select one of the
		# cups that was just picked up, the crab will keep subtracting one
		# until it finds a cup that wasn't just picked up. If at any point
		# in this process the value goes below the lowest value on any cup's label,
		# it wraps around to the highest value on any cup's label instead."
		destination_cup = self.get_smaller_or_max_cup(picked_up_cups)

		# "The crab places the cups it just picked up so that they are
		# immediately clockwise of the destination cup. They keep the same
		# order as when they were picked up."
		self.set_down_cups(destination_cup, picked_up_cups)

		# "The crab selects a new current cup: the cup which is immediately
		# clockwise of the current cup."
		# (current is first index)
		self.current_cup = self.get_next(self.current_cup)

	def pickup_cups(self):
		sublist_to_remove = self.get_next(self.current_cup)
		last_in_sublist_to_remove = self.get_next(self.get_next(sublist_to_remove))
		after_sublist = self.get_next(last_in_sublist_to_remove)
		self.set_next(last_in_sublist_to_remove, None)
		self.set_next(self.current_cup, after_sublist)
		return sublist_to_remove

	def set_down_cups(self, destination_cup, picked_up_cups):
		after_set_down = self.get_next(destination_cup)
		self.set_next(destination_cup, picked_up_cups)
		self.set_next(self.get_next(self.get_next(picked_up_cups)), after_set_down)

	def get_smaller_or_max_cup(self, picked_up_cups):
		excluded_labels = set(self.cups_to_label_list(picked_up_cups))
		cup_index = (self.current_cup['label'] - 1 - 1) % len(self.index)
		while True:
			if cup_index+1 not in excluded_labels:
				return self.index[cup_index]
			cup_index = (cup_index - 1) % len(self.index)

	def to_label_list(self):
		return self.cups_to_label_list(self.current_cup)

	def cups_to_label_list(self, cups):
		result = []
		first_cup_label = cups['label']
		result.append(first_cup_label)
		next_cup = self.get_next(cups)
		while next_cup != None and next_cup['label'] != first_cup_label:
			result.append(next_cup['label'])
			next_cup = self.get_next(next_cup)
			# print(next_cup)
		return result

	def get_next(self, cup):
		if cup['next_cup'] == None:
			return None
		else:
			return self.index[cup['next_cup']-1]

	def set_next(self, cup, next_cup):
		if next_cup == None:
			cup['next_cup']	= None
		else:
			cup['next_cup']	= next_cup['label']

	def set_product_of_two_labels_after_1(self):
		product = 1
		cup = self.get_next(self.index[0])
		product *= cup['label']
		cup = self.get_next(cup)
		product *= cup['label']
		return product
