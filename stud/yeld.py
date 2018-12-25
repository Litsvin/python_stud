import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[{x}, {y}]; ".format(x=self.x, y=self.y)


class Route:
    def __init__(self, pts):
        self.pts = pts


def get_points(n):
    for _ in range(n):
        yield Point(random.randint(0, 100), random.randint(0, 100))


points = list()
for i in get_points(100):
    points.append(i)
print(points)
