class Cell:
    def __init__(self, num_partition):
        self.num_partition = num_partition

    def __add__(self, other):
        return Cell(self.num_partition + other.num_partition)

    def __sub__(self, other):
        if self.num_partition >= other.num_partition:
            return Cell(self.num_partition - other.num_partition)
        else:
            raise ValueError("Количество ячеек в первой клетке меньше чем во второй")

    def __mul__(self, other):
        return Cell(self.num_partition * other.num_partition)

    def __floordiv__(self, other):
        return Cell(self.num_partition // other.num_partition)

    def __str__(self):
        return f'Количество ячеек в клетке = {self.num_partition}'

    def make_order(self, num):
        cell = ''
        count = 1
        while count <= self.num_partition:
            cell += '*'
            if count % num == 0:
                cell += '\n'
            count += 1
        return cell


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_order(3))
