import time
from collections import Iterable

def flatten2(iterable):
    return list(filter(lambda x: x != None, flattener2(iterable)))
 
 
def flattener2(iterable): 
    for element in iterable:
        try:
            yield from flattener(element)
        except:
            yield element

start_time = time.perf_counter()
flatten2([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
print("--- %.10f seconds ---" % (time.perf_counter() - start_time))

def flatten(iterable):
        return list(filter(lambda x: x != None, flattener(iterable)))


def flattener(iterable):
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flattener(element)
        else:
            yield element

        
start_time = time.perf_counter()
flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
print("--- %.10f seconds ---" % (time.perf_counter() - start_time))
