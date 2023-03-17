from Python_Code.venv.Circle import Circle
from Python_Code.venv.Newton_Method import shift_distance


class Coaster(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.overlap_area = None
        self.distance = None

    def overlap(self):
        self.overlap_area =  self.area() / 2
        return self.overlap_area

    def shift_distance(self, x0):
        self.distance = shift_distance(x0, self.radius)
        return self.distance

    def display(self):
        string = ""
        string += f"Coaster with radius {self.radius}\n"
        string += f"Area: {self.area()}\n"
        string += f"Circumference: {self.circumference()}\n"
        if self.overlap_area is not None:
            string += f"Overlap area: {self.overlap_area}\n"
        if self.distance is not None:
            string+= f"Distance needed to shift coaster for overlap to be half the area: {self.distance}\n"
        return string

    def get_radious(self):
        return self.radius
