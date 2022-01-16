from itertools import zip_longest


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        res = []
        for el1, el2 in zip_longest(self.matrix_list, other.matrix_list, fillvalue=[0]):
            tmp = []
            for el3, el4 in zip_longest(el1, el2, fillvalue=0):
                tmp.append(el3+el4)
            res.append(tmp)
        return Matrix(res)

    def __str__(self):
        matrix = ''
        for el1 in self.matrix_list:
            for el2 in el1:
                matrix += f'{el2}\t'
            matrix += f'\n'
        return matrix


test_list1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
test_matrix1 = Matrix(test_list1)
print(test_matrix1)
test_list2 = [[5, 4, 15], [22, -8, 0], [54, -10, 8]]
test_matrix2 = Matrix(test_list2)
print(test_matrix2)
print(test_matrix1 + test_matrix2)
