def flatten(iterable):
    return list(filter(lambda x: x != None, flattener(iterable)))
 
 
def flattener(iterable): 
    for element in iterable:
        try:
            yield from flattener(element)
        except:
            yield element

