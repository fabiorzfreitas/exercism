def find(search_list, value):
    if not value in search_list:
        raise ValueError("value not in array")
    if search_list[len(search_list) // 2] == value:
        return len(search_list) // 2
    elif search_list[len(search_list) // 2] > value:
        return find(search_list[:(len(search_list) // 2)], value)
    elif search_list[len(search_list) // 2] < value:
        return find(search_list[(len(search_list) // 2):], value) + len(search_list) // 2

