def response(hey_bob=''):
    if hey_bob.rstrip() == '':
        return "Fine. Be that way!"
    elif hey_bob.rstrip().endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
