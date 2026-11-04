def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    data: dict = {}
    for point, letter_list in legacy_data.items():
        for letter in letter_list:
            data[letter.lower()] = point
    return data
