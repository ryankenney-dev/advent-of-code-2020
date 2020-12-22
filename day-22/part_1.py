import math

def parse_input(input):
	hands = []
	hand_strings = input.split('\n\n')
	for hand_string in hand_strings:
		lines = hand_string.splitlines()
		hands.append(list(map(lambda l: int(l), lines[1:])))
	return hands

def play_round(hand1, hand2):
	card1 = hand1.pop(0)
	card2 = hand2.pop(0)
	if card1 > card2:
		hand1.extend([card1, card2])
	elif card1 < card2:
		hand2.extend([card2, card1])
	else:
		raise Exception('Should not happen')

def play_whole_game(hand1, hand2):
	while len(hand1) > 0 and len(hand2) > 0:
		play_round(hand1, hand2)
	return max(compute_score(hand1), compute_score(hand2))

def compute_score(hand):
	score = 0
	for i in range(0, len(hand)):
		score += (i+1) * hand[len(hand)-i-1]
	return score