class Spiral():

    def __init__(self, size):
        self.matrix = self.populate(size)
        self.direction = 0
        self.row = 0
        self.position = 0
        self.count = 2
        self.position_export = 0
        self.row_export = 0
        if size != 0:
            self.matrix[0][0] = 1
    
    def right(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row][position + index + 1] == None:
                    matrix[row][position + index + 1] = count
                    count += 1
                    self.position_export = position + index + 1
                
            except:
                break
        self.row = row
        self.position = self.position_export
        self.count = count
    
    def down(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row + index + 1][position]  == None:
                    matrix[row + index + 1][position] = count
                    count += 1
                    self.row_export = row + index + 1
            except:
                break
        self.row = self.row_export
        self.position = position
        self.count = count
    
    def left(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row][position - index - 1] == None:
                    if position - index >= 0:
                        matrix[row][position - index - 1] = count
                        count += 1
                        self.position_export = position - index - 1
            except:
                break
        self.row = row
        self.position = self.position_export
        self.count = count
    
    def up(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row - index][position]  == None:
                    matrix[row - index][position] = count
                    count += 1
                    self.row_export = row - index
            except:
                break
        self.row = self.row_export
        self.position = position
        self.count = count
    
    def populate(self, size: int):
        spiral: list = [[None for x in range(size)] for x in range(size)]
        return spiral

    def builder(self):
        count = 0
        while any(None in sublist for sublist in self.matrix):
            functions: dict[int, function] = {
                0: self.right(self.matrix, self.row, self.position, self.count), 
                1: self.down(self.matrix, self.row, self.position, self.count), 
                2: self.left(self.matrix, self.row, self.position, self.count), 
                3: self.up(self.matrix, self.row, self.position, self.count)
                }
            functions[count % 4]
            count += 1
        return self.matrix
        

def spiral_matrix(size: int):
    return Spiral(size).builder()

