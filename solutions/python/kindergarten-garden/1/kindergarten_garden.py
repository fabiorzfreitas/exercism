student_list: list[str] = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

class Garden:
    def __init__(self, diagram: str, students: list = student_list):
        self.diagram: list = diagram.split('\n')
        self.students: list = sorted(students)
    
    def plants(self, student: str):
        plant_names: dict = {'V': 'Violets', 'C': 'Clover', 'R': 'Radishes', 'G': 'Grass'}
        index: int = self.students.index(student)
        output: list = []
        output.append(plant_names[self.diagram[0][2 * index]])
        output.append(plant_names[self.diagram[0][(2 * index) + 1]])
        output.append(plant_names[self.diagram[1][2 * index]])
        output.append(plant_names[self.diagram[1][(2 * index) + 1]])
        return output



