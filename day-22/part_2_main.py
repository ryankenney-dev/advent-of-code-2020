import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

hands = part_2.parse_input(message)
winning_score = part_2.play_whole_game(hands[0], hands[1])

print("")
print("[[[ Winning Score: %s ]]]" % winning_score)
print("")
