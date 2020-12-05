import part_2
import sys

with open(sys.argv[1], 'r') as f:
    part_2.find_my_seat(f.readlines())
