class Matrix:
    def __init__(self, param_lists):
        self.param_lists = param_lists
        pass

    def __str__(self, add_list):
        el_str = ''
        for el in add_list:
            el = [str(i) for i in el]
            el_str += ','.join(el).replace(',', ' ') + '\n'
        return el_str

    def __add__(self, other):
        new_matrix = []
        for i, el in enumerate(self.param_lists):
            if len(self.param_lists) != len(other.param_lists) or len(el) != len(other.param_lists[i]):
                print('Сложение матриц невозможно!')
                exit()
            else:
                new_matrix.append([val + other.param_lists[i][key] for key, val in enumerate(el)])
        return self.__str__(new_matrix)


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[12, 32, 4], [45, 14, -7], [11, 12, 18]]
a_obj = Matrix(a)
b_obj = Matrix(b)
print(a_obj + b_obj)
