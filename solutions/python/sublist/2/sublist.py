"""
This iteration is a recreation of AndreaRaccagni's solution, submited in order to fixate my knowledge
"""
SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if list_one == list_two:
        return 'EQUAL'
    elif issublist(list_one, list_two):
        return 'SUBLIST'
    elif issublist(list_two, list_one):
        return 'SUPERLIST'
    else:
        return 'UNEQUAL'


def issublist(smaller, bigger):
    for i in range(len(bigger) - len(smaller) + 1):
        if not smaller or smaller == bigger[i:i+len(smaller)]:
            return True
    return False