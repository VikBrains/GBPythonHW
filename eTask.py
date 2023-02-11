class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        result = []
        for line in self.list:
            result.append(' '.join([str(k) for k in line]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.list) == len(other.list):
            result = []
            for i, row in enumerate(self.list):
                new_list = list(map(lambda x, y: x + y, row, other.list[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return


m_lists_01 = [[1, 2, 3], [3, 3, 3], [4, 3, 2]]
m_lists_02 = [[2, 5, 5], [4, 3, 3], [1, 1, 2]]

matrix01 = Matrix(m_lists_01)
matrix02 = Matrix(m_lists_02)
matrix03 = matrix01 + matrix02

print(matrix01, end='\n\n')
print(matrix02, end='\n\n')
print(matrix03)
