def append(list1, list2):
    new_list = list1 + list2
    return new_list


def concat(lists):
    new_list = []
    for list in lists:
        new_list += list
    return new_list


def filter(function, list):
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list


def length(list):
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    new_list = []
    for item in list:
        new_list.append(function(item))
    return new_list


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
