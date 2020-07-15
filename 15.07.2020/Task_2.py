class Road:
    def __init__(self, _length, _width):
        self._length = _length
        _length = 25
        self._width = _width
        _width = 5000


    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())