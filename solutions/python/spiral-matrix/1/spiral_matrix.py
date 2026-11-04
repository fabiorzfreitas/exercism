class spiral():
    direction = 0
    row = 0
    position = 0
    count = 2
    position_export = 0
    row_export = 0


    def __init__(self, size):
        self.matrix = self.populate(size)
        self.matrix[0][0] = 1

    
    def right(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row][position + index + 1] == None:
                    matrix[row][position + index + 1] = count
                    count += 1
                    position_export = position + index + 1
                
            except:
                break
        self.row = row
        self.position = position_export
        self.count = count
    
    
    def down(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row + index + 1][position]  == None:
                    matrix[row + index + 1][position] = count
                    count += 1
                    row_export = row + index + 1
            except:
                break
        self.row = row_export
        self.position = position
        self.count = count
    
    
    def left(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row][position - index - 1] == None:
                    if position - index >= 0:
                        matrix[row][position - index - 1] = count
                        count += 1
                        position_export = position - index - 1
            except:
                break
        self.row = row
        self.position = position_export
        self.count = count
    
    
    def up(self, matrix: list[list], row: int, position: int, count: int):
        for index, square in enumerate(matrix[row]):
            try:
                if matrix[row - index][position]  == None:
                    matrix[row - index][position] = count
                    count += 1
                    row_export = row - index
            except:
                break
        self.row = row_export
        self.position = position
        self.count = count
    
    
    def populate(self, size: int):
        spiral: list = [[None for x in range(size)] for x in range(size)]
        return spiral
    

    def builder(self):
        while any(None in sublist for sublist in self.matrix):
            if self.direction == 0:
                self.right(self.matrix, self.row, self.position, self.count)
                self.direction += 1
            elif self.direction == 1:
                self.down(self.matrix, self.row, self.position, self.count)
                self.direction += 1
            elif self.direction == 2:
                self.left(self.matrix, self.row, self.position, self.count)
                self.direction += 1
            elif self.direction == 3:
                self.up(self.matrix, self.row, self.position, self.count)
                self.direction -= 3
        return self.matrix
        

def spiral_matrix(size: int):
    if size == 0:
        return []
    instance = spiral(size)
    return instance.builder()

