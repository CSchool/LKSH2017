def check_traumatic(items, facts):
    if 'has_fight_kitchen' in facts and 'lead_programmer_card_taken' in facts:
        return True
    return False