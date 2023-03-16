from Python_Code.venv.Coaster import Coaster


class CHEERS:
    def __init__(self):
        self.coaster1 = None
        self.coaster2 = None

    def get_input(self):
        r1 = float(input("Enter the radius of coaster 1: "))
        r2 = float(input("Enter the radius of coaster 2: "))
        self.coaster1 = Coaster(r1)
        self.coaster2 = Coaster(r2)

    def display_output(self):
        print("Coaster 1:")
        self.coaster1.display()
        print("Coaster 2:")
        self.coaster2.display()
        print("Overlap area:", self.coaster1.overlap(self.coaster2))
        print("Distance needed to shift:", self.coaster1.shift_distance(self.coaster2))

    def run(self):
        self.get_input()
        self.display_output()


if __name__ == '__main__':
    cheers = CHEERS()
    cheers.run()
