def parse_to_numbers(message):
    return list(map(lambda s: int(s), message.split(',')))

def compute_until_2020(initial_numbers):
    turn = 0
    spoken_number_to_last_turn = {}
    for number in initial_numbers:
        #print('Speak: %s' % number)
        spoken_number_to_last_turn[number] = turn
        turn += 1
    # NOTE: We're not handling the case where the initial
    # numbers contain a duplicate, but the proble does not
    # contain that.
    number = 0
    for turn in range(turn, 2019):
        #print('Speak: %s' % number)
        if number in spoken_number_to_last_turn:
            next_number = turn - spoken_number_to_last_turn[number]
        else:
            next_number = 0
        spoken_number_to_last_turn[number] = turn
        number = next_number
    return number
