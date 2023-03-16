from Python_Code.venv.Circle import Circle


class Coaster(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.overlap_area = None
        self.distance = None

    def overlap(self, other):

        return self.overlap_area

    def shift_distance(self, other):

        return self.distance

    def display(self):
        print(f"Coaster with radius {self.radius}")
        print(f"Area: {self.area()}")
        print(f"Circumference: {self.circumference()}")
        if self.overlap_area is not None:
            print(f"Overlap area: {self.overlap_area}")
        if self.distance is not None:
            print(f"Distance needed to shift coaster for overlap to be half the area: {self.distance}")
