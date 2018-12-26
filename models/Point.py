class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __str__(self):
        return "Point: [x, y, z] = [{0}, {1}, {2}]".format(self.x, self.y, self.z)

