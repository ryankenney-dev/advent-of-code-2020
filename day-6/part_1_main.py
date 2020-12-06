import part_1
import sys

family_responses = part_1.read_input_file_to_family_responses(sys.argv[1])
result = part_1.family_responses_to_sum_of_responses(family_responses)

print("")
print("[[[ Total Count: %s ]]]" % result)
print("")
