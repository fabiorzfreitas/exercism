# Score categories.
# Change the values as you see fit.
def YACHT(dice):
    if len(set(dice)) == 1:
        return 50
    else:
        return 0


def ONES(dice):
    return dice.count(1)


def TWOS(dice):
    return dice.count(2) * 2


def THREES(dice):
    return dice.count(3) * 3


def FOURS(dice):
    return dice.count(4) * 4


def FIVES(dice):
    return dice.count(5) * 5


def SIXES(dice):
    return dice.count(6) * 6


def FULL_HOUSE(dice):
    if len(set(dice)) == 2:
        if sorted(dice)[1] != sorted(dice)[3]:
            return sum(dice)
        else:
            return 0
    else:
        return 0


def FOUR_OF_A_KIND(dice):
    if len(set(dice)) <= 2:
        if sorted(dice)[1] == sorted(dice)[3]:
            if sorted(dice)[0] != sorted(dice)[1]:
                return sum(sorted(dice)[1:5])
            else:
                return sum(sorted(dice)[0:4])
        else:
            return 0
    else:
        return 0


def LITTLE_STRAIGHT(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    else:
        return 0


def BIG_STRAIGHT(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0


def CHOICE(dice):
    return sum(dice)


def score(dice, category):
    return category(dice)
