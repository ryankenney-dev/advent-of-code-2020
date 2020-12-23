import part_2
import sys

with open(sys.argv[1], 'r') as f:
    message = f.read()

game = part_2.Game(message, 1000000)
for i in range(0, 10000000):
	game.run_cycle()
result = game.set_product_of_two_labels_after_1()

print("")
print("[[[ Result: %s ]]]" % result)
print("")
