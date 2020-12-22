import part_1
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

hands = part_1.parse_input(message)
winning_score = part_1.play_whole_game(hands[0], hands[1])

print("")
print("[[[ Winning Score: %s ]]]" % winning_score)
print("")
