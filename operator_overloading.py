class OperatorOverloading:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return OperatorOverloading(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return OperatorOverloading(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return OperatorOverloading(self.x * other.x, self.y * other.y)

    def __mod__(self, other):
        return OperatorOverloading(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return OperatorOverloading(self.x ** other.x, self.y ** other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"OperatorOverloading({self.x}, {self.y})"


v1 = OperatorOverloading(1, 1)
v2 = OperatorOverloading(2, 1)

print(v1 * v2)
