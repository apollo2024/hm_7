class Vector:
    x = 0.0
    y = 0.0
    z = 0.0

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def getz(self):
        return self.z