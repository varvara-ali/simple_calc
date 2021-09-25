class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return (self.x)

    def get_y(self):
        return (self.y)

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f'{self.name}({self.x}, {self.y})'

    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, rgb=(0, 0, 0)):
        super().__init__(name, x, y)
        self.rgb = rgb

    def get_color(self):
        return self.rgb

    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, (255 - self.rgb[0], 255 - self.rgb[1], 255 - self.rgb[2]))


point_X = Point('X', 5, -7)
print(point_X)
point_A = ColoredPoint('A', 0, 3, (255, 204, 0))
print(point_A, point_A.get_color())
point_B = ~point_A
print(point_B, point_B.get_color())
point_O = ~ColoredPoint('O', 0, 0)
print(point_O, point_O.get_color())
