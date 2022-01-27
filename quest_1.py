class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for i in self.my_list:
            for j in i:
                print(f'{j:5}', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list)):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


mat_1 = Matrix([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
mat_2 = Matrix([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
print(mat_1 + mat_2)
