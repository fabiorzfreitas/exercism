verses: list = [
    'horse and the hound and the horn that belonged to',
    'farmer sowing his corn that kept',
    'rooster that crowed in the morn that woke',
    'priest all shaven and shorn that married',
    'man all tattered and torn that kissed',
    'maiden all forlorn that milked',
    'cow with the crumpled horn that tossed',
    'dog that worried',
    'cat that killed',
    'rat that ate',
    'malt that lay in',
    'house that Jack built.'
]

def line_builder(start: int, verse: int):
    if verse == 0:
        return ''    
    elif verse == start:
        return 'This is the ' + verses[-verse] + line_builder(start, verse - 1)
    else:
        return ' the ' + verses[-verse] + line_builder(start, verse - 1)
    

def recite(start_verse: int, end_verse: int):
    return [line_builder(x, x) for x in range(start_verse, end_verse + 1)]

