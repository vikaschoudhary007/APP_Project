from Python_Code.venv.PI import PI


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI() * self.radius ** 2

    def circumference(self):
        return 2 * PI() * self.radius
