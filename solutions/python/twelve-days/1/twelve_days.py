gifts: dict[int, tuple[str, str]] = {
    0: ('a Partridge in a Pear Tree', 'first'),
    1: ('two Turtle Doves', 'second'),
    2: ('three French Hens', 'third'),
    3: ('four Calling Birds', 'fourth'),
    4: ('five Gold Rings', 'fifth'),
    5: ('six Geese-a-Laying', 'sixth'),
    6: ('seven Swans-a-Swimming', 'seventh'),
    7: ('eight Maids-a-Milking', 'eighth'),
    8: ('nine Ladies Dancing', 'ninth'),
    9: ('ten Lords-a-Leaping', 'tenth'),
    10: ('eleven Pipers Piping', 'eleventh'),
    11: ('twelve Drummers Drumming', 'twelfth')
}


def verse(start_verse: int, end_verse: int) -> str:
    verses: list = [f'On the {gifts[start_verse][1]} day of Christmas my true love gave to me: ']
    if end_verse == 0:
        verses.append(f'{gifts[0][0]}.')
        return ''.join(verses)
    reversed_gifts = [f'{gifts[x][0]}, ' for x in range(end_verse, 0, -1)]
    return ''.join(verses + reversed_gifts + [f'and {gifts[0][0]}.'])


def recite(start_verse: int, end_verse: int) -> list[str]:
    output: list = []
    for i in range (start_verse - 1, end_verse):
        print(i)
        output.append(verse(i,i))
    return output

