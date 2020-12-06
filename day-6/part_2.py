def read_input_file_to_family_responses(input_file_path):
    with open(input_file_path, 'r') as f:
        return read_input_to_family_responses(f.read())

def read_input_to_family_responses(input):
    return input.split('\n\n')

def family_responses_to_question_ids(family_responses):
    question_id_counts = {}
    for individual_responses in family_responses.splitlines():  
        for question in individual_responses:
            if question not in question_id_counts:
                question_id_counts[question] = 0
            question_id_counts[question] = question_id_counts[question] + 1
    question_ids = set()
    for question_id in question_id_counts.keys():
        if question_id_counts[question_id] >= len(family_responses.splitlines()):
            question_ids.add(question_id)
    return question_ids

def family_responses_to_sum_of_responses(family_responses):
    sum_of_responses = 0
    for family_response in family_responses:
        question_ids = family_responses_to_question_ids(family_response)
        sum_of_responses = sum_of_responses + len(question_ids)
    return sum_of_responses


