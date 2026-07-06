class Points:


    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


point = Points(5, 8)
print(point)
print(repr(point))