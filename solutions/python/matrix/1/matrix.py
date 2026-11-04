class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.list_of_lists: list[list[int]] = [[int(char) for char in line.split(' ')] for line in matrix_string.split('\n')]
        
    def row(self, index: int) -> list[int]:
        return self.list_of_lists[index - 1]

    def column(self, index: int) -> list[int]:
        return [row[index - 1] for row in self.list_of_lists]
