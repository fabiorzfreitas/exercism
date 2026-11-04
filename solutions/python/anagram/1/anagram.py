def find_anagrams(word: str, candidates: list[str]) -> list:
    return [candidate for candidate in candidates if candidate.lower() != word.lower() and sorted(candidate.lower()) == sorted(word.lower())]
    