class Point:

    def __init__(self, st, x, y):
        self.st = st
        self.x = x
        self.y = y

    def __str__(self):
        return self.st + '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __repr__(self):
        return 'Point(' + "'" + self.st + "'" + ', ' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, other):
        if self.st == other.st and self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.st != other.st or self.x != other.x or self.y != other.y:
            return True
        return False

    def __lt__(self, other):
        if self.st < other.st or self.x < other.x or self.y < other.y:
            return True
        return False

    def __le__(self, other):
        if self.st <= other.st and self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __gt__(self, other):
        if self.st > other.st or self.x > other.x or self.y > other.y:
            return True
        return False

    def __ge__(self, other):
        if self.st >= other.st and self.x >= other.x and self.y >= other.y:
            return True
        return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y