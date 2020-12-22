import math
import copy

def parse_input(input):
	hands = []
	hand_strings = input.split('\n\n')
	for hand_string in hand_strings:
		lines = hand_string.splitlines()
		hands.append(list(map(lambda l: int(l), lines[1:])))
	return hands

def play_round(hands):

	# TODO: Remove debug
	print('play_round hands: %s' % hands)

	# Draw cards
	cards = []
	for i, hand in enumerate(hands):
		cards.append(hand.pop(0))

	# Check for recursive game
	enough_for_recurse = True
	for card, hand in zip(cards, hands):
		if card > len(hand):
			enough_for_recurse = False
			break

	# Launch recursive game
	if enough_for_recurse:
		winner = play_whole_game(copy.deepcopy(hands))

	# Identify winner by current cards
	else:
		winner = cards.index(max(cards))

	# Distribute cards to winner
	if winner == 0:
		hands[0].extend([cards[0], cards[1]])
	elif winner == 1:
		hands[1].extend([cards[1], cards[0]])
	else:
		raise Exception('Should not happpen')

# TODO: Remove debug
game_id = 0

def play_whole_game(hands):

	# TODO: Remove debug
	global game_id
	game_id += 1
	print('[GAME: %s] play_whole_game hands: %s' % (game_id, hands))

	hand_history = [set(),set()]
	# While no hand empty...
	while all(list(map(lambda h: len(h) > 0, hands))):
		# If any hand has been played before,
		# by the same player, player 1 wins
		for hand, history in zip(hands, hand_history):
			if hand_to_string(hand) in history:
				return 0
			history.add(hand_to_string(hand))
		play_round(hands)

	scores = []
	for hand in hands:
		scores.append(compute_score(hand))
	return scores.index(max(scores))

def compute_score(hand):
	score = 0
	for i in range(0, len(hand)):

		# TODO: Remove debug
		print('hand: %s' % hand)
		print('%s * %s = %s' % ((i+1), hand[len(hand)-i-1], (i+1) * hand[len(hand)-i-1]))

		score += (i+1) * hand[len(hand)-i-1]
	return score

def hand_to_string(hand):
	return ''.join(list(map(lambda c: str(c), hand)))