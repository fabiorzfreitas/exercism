import time
from collections import Iterable
import timeit


def flatten2(iterable):
    return list(filter(lambda x: x != None, flattener2(iterable)))
 
 
def flattener2(iterable): 
    for element in iterable:
        try:
            yield from flattener2(element)
        except:
            yield element

start_time = time.perf_counter()
flatten2([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
flatten2_time = "%.10f" % (time.perf_counter() - start_time)

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
flatten_time = "%.10f" % (time.perf_counter() - start_time)

print(float(flatten_time)/float(flatten2_time))

t2 = min(timeit.repeat('flatten2([1, [2, [[3]], [4, [[5]]], 6, 7], 8])', repeat=10000, number=1, globals=globals()))
t1 = min(timeit.repeat('flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8])', repeat=10000, number=1, globals=globals()))

print(t1/t2)