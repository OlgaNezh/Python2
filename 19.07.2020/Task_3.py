class Cell():
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return 'Cell(size:{})'.format(self.size)

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        new_size = self.size - other.size
        if new_size > 0:
            return Cell(new_size)
        else:
            raise ArithmeticError(new_size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, rowsize):
        excess = self.size
        strres = ' '
        while excess:
            the_row_size = rowsize if excess >= rowsize else excess
            strres += '*' * the_row_size
            excess -= the_row_size
        return strres


c5 = Cell(5)
c6 = Cell(6)

print('add: c5 + c6:', c5 + c6)
print('sub: c6 - c5:', c6 - c5)

try:
    print(c5 - c6)
except ArithmeticError:
    print('sub: c5 - c6: Wrong sub args')

print('mul: c5 * c6:', c5 * c6)
print('div: c5 / c6:', c5 / c6)
print('div: c6 / c5:', c6 * c5)

