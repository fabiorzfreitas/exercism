def score(x, y):
    """
    This iteration is a recreation of astrorip's solution
    submited to fixate what I learnt from their code
    """
    r = (x ** 2 + y ** 2) ** 0.5
    return (r <= 10) * 1 + (r <= 5) * 4 + (r <= 1) * 5