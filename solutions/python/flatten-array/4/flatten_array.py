import time
import timeit
from collections import Iterable


def flatten2(iterable):
    return list(filter(lambda x: x != None, flattener2(iterable)))
 
 
def flattener2(iterable): 
    for element in iterable:
        try:
            yield from flattener2(element)
        except:
            yield element

t2_list = []
count = 0
while count <= 10000:
    start_time = time.perf_counter()
    flatten2([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
    flatten2_time = time.perf_counter() - start_time
    t2_list.append(flatten2_time)
    count += 1

def flatten(iterable):
        return list(filter(lambda x: x != None, flattener(iterable)))


def flattener(iterable):
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flattener(element)
        else:
            yield element

        
t1_list = []
count = 0
while count <= 10000:
    start_time = time.perf_counter()
    flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8])
    flatten_time = time.perf_counter() - start_time
    t1_list.append(flatten_time)
    count += 1

print(min(t1_list)/min(t2_list))

t2 = min(timeit.repeat('flatten2([1, [2, [[3]], [4, [[5]]], 6, 7], 8])', repeat=10000, number=1, globals=globals()))
t1 = min(timeit.repeat('flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8])', repeat=10000, number=1, globals=globals()))

print(t1/t2)