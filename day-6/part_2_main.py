import part_2
import sys

family_responses = part_2.read_input_file_to_family_responses(sys.argv[1])
result = part_2.family_responses_to_sum_of_responses(family_responses)

print("")
print("[[[ Total Count: %s ]]]" % result)
print("")
