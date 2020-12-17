import re

def parse_message(message):
    sections = message.split('\n\n')
    rules_section = sections[0]
    my_ticket_section = sections[1]
    nearby_tickets_section = sections[2]

    rules = {}
    for line in rules_section.splitlines():
        pattern = re.compile(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')
        match = pattern.match(line)
        if not match:
            raise Exception('Invalid line: %s' % line)
        rules[match.group(1)] = [
            ( int(match.group(2)), int(match.group(3)) ),
            ( int(match.group(4)), int(match.group(5)) )]


    my_ticket_line = my_ticket_section.splitlines()[1]
    my_ticket = list(map(lambda f: int(f), my_ticket_line.split(',')))

    nearby_tickets = []
    for line in nearby_tickets_section.splitlines()[1:]:
        nearby_tickets.append(list(map(lambda f: int(f), line.split(','))))

    return { 'rules': rules, 'my_ticket': my_ticket, 'nearby_tickets': nearby_tickets }
        
def find_valid_nearby_tickets(ticket_data):
    valid_tickets = []
    for ticket in ticket_data['nearby_tickets']:
        ticket_valid = True
        for field_value in ticket:
            if not matches_any_rule(field_value, ticket_data['rules'].values()):
                ticket_valid = False
                break
        if not ticket_valid:
            continue
        valid_tickets.append(ticket)
    return valid_tickets

def matches_any_rule(field_value, rules):
    for rule in rules:
        if in_rule_ranges(field_value, rule):
            return True
    return False

def identify_field_to_rule_mapping(ticket_data):
    possible_rules_per_field = [None] * len(ticket_data['my_ticket'])

    # Initialize indexes of possible field mappings to all possibilities
    for field_id in range(0, len(ticket_data['my_ticket'])):
        possible_rules_per_field[field_id] = set()
    for rule_name in ticket_data['rules'].keys():
        for field_id in range(0, len(ticket_data['my_ticket'])):
            possible_rules_per_field[field_id].add(rule_name)

    nearby_tickets = find_valid_nearby_tickets(ticket_data)
    solved_field_ids = set()
    for ticket in nearby_tickets:
        for field_id in range(0, len(ticket)):
            rules_to_remove = []

            # Identify ranges that couldn't apply to this field
            for rule in possible_rules_per_field[field_id]:
                if not in_rule_ranges(ticket[field_id], ticket_data['rules'][rule]):
                    rules_to_remove.append(rule)

            # Remove ranges that couldn't apply to this field
            for r in rules_to_remove:
                possible_rules_per_field[field_id].discard(r)

            # Identify all fields with exactly one solution and eliminate
            # those from all others (repeatedly).
            propagate_solved_fields(possible_rules_per_field, solved_field_ids)

    return list(map(lambda s: list(s)[0], possible_rules_per_field))

def propagate_solved_fields(possible_rules_per_field, solved_field_ids):
    while True:
        solved_id = find_newly_solved_field_id(possible_rules_per_field, solved_field_ids)
        if solved_id == None:
            break
        rule_to_discard = list(possible_rules_per_field[solved_id])[0]
        for other_field_id in range(0, len(possible_rules_per_field)):
            if other_field_id == solved_id:
                continue
            possible_rules_per_field[other_field_id].discard(rule_to_discard)
        solved_field_ids.add(solved_id)

def find_newly_solved_field_id(possible_rules_per_field, solved_field_ids):
    for field_id in range(0, len(possible_rules_per_field)):
        if field_id in solved_field_ids:
            continue
        if len(possible_rules_per_field[field_id]) == 1:
            return field_id
    return None

def in_rule_ranges(field_value, rule):
    for r in rule:
        if field_value >= r[0] and field_value <= r[1]:
            return True
    return False

def compute_product_departure_fields(ticket_data):
    field_to_rule_mapping = identify_field_to_rule_mapping(ticket_data)
    my_ticket = ticket_data['my_ticket']
    product = 1
    for field_id in range(0, len(my_ticket)):
        if not field_to_rule_mapping[field_id].startswith('departure '):
            continue
        product *= my_ticket[field_id]
    return product