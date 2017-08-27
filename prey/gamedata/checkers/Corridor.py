# kitchen and cargo bay are opened
def cargo_opened_card_founded(items, facts):
    return 'AccessCard' in items and 'cargo_bay_opened' in facts


# kitchen is opened, cargo bay is closed
def cargo_closed_card_founded(items, facts):
    return 'AccessCard' in items and 'cargo_bay_opened' not in facts


# kitchen is closed, cargo bay is opened
def cargo_opened_card_not_founded(items, facts):
    return 'AccessCard' not in items and 'cargo_bay_opened' in facts


# kitchen and cargo bay are closed
def cargo_closed_card_not_existed(items, facts):
    return 'AccessCard' not in items and 'cargo_bay_opened' not in facts

