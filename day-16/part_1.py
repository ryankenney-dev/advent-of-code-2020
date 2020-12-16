import re

def parse_message(message):
    sections = message.split('\n\n')
    rules_section = sections[0]
    my_ticket_section = sections[1]
    nearby_tickets_section = sections[2]

    rules = []
    for line in rules_section.splitlines():
        pattern = re.compile(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')
        match = pattern.match(line)
        if not match:
            raise Exception('Invalid line: %s' % line)
        rules.append({
            'name': match.group(1),
            'ranges': [(
                int(match.group(2)), int(match.group(3))
            ),(
                int(match.group(4)), int(match.group(5))
            )]
        })

    nearby_tickets = []
    for line in nearby_tickets_section.splitlines()[1:]:
        nearby_tickets.append(list(map(lambda f: int(f), line.split(','))))

    return { 'rules': rules, 'nearby_tickets': nearby_tickets }
        
def find_invalid_nearby_ticket_field_values(ticket_data):
    invalid_field_values = []
    for ticket in ticket_data['nearby_tickets']:
        for field_value in ticket:
            found_valid_range = False
            for rule in ticket_data['rules']:
                if found_valid_range:
                    break
                for value_range in rule['ranges']:
                    if field_value >= value_range[0] and field_value <= value_range[1]:
                        found_valid_range = True
                        break
            if found_valid_range:
                continue
            invalid_field_values.append(field_value)
    return invalid_field_values
