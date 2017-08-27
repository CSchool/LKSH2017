def check_has_map(items, facts, achievments):
    return 'can_view_map' in facts

def check_did_suicide(items, facts, achievments):
    if 'Ending_2' in achievments or 'Ending_16' in achievments:
        return True
    return False

def check_all_bad_endings(items, facts, achievments):
    endings = 16
    for i in range(1, endings + 1):
        if ("Ending_%d" % i) not in achievments:
            return False
    return True

def check_double_flamethrower(items, facts, achievments):
    return 'double_flamethrower' in facts