def read_input_file_to_family_responses(input_file_path):
    with open(input_file_path, 'r') as f:
        return read_input_to_family_responses(f.read())

def read_input_to_family_responses(input):
    return input.split('\n\n')

def family_responses_to_question_ids(family_responses):
    question_ids = set()
    for individual_responses in family_responses.splitlines():  
        for question in individual_responses:
            question_ids.add(question)
    return question_ids

def family_responses_to_sum_of_responses(family_responses):
    sum_of_responses = 0
    for family_response in family_responses:
        question_ids = family_responses_to_question_ids(family_response)
        sum_of_responses = sum_of_responses + len(question_ids)
    return sum_of_responses


