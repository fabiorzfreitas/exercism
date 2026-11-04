class HighScores:
    def __init__(self, scores: list[int]):
        self.scores: list[int] = scores

    def latest(self) -> int:
        return self.scores[-1]

    def personal_best(self) -> int:
        return max(self.scores)

    def personal_top_three(self) -> list[int]:
        sorted_list: list[int] = sorted(self.scores)
        return [sorted_list.pop() for i in range(3)] if len(self.scores) >= 3 else [sorted_list.pop() for j in range(len(self.scores))]
