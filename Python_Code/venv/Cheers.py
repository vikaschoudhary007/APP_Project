from Python_Code.venv.Coaster import Coaster
from dicttoxml import dicttoxml
import matplotlib.pyplot as plt
from Python_Code.venv.PI import PI


class CHEERS:
    def __init__(self):
        self.coaster1 = None
        self.x0 = PI()/2

    def get_input(self):
        try:
            r1 = float(input("Enter the radius of coaster: "))
            self.coaster1 = Coaster(r1)
        except ValueError:
            print("Invalid input. Please enter a valid radius.")

    def get_newton_input(self):
        try:
            self.x0 = float(input("Enter the starting point for newton method: "))
        except ValueError:
            print("Invalid input. Please enter a valid starting point for newton method.")

    def display_output(self):
        string = ""
        string += f"Coaster 1:\n"
        string += f"{self.coaster1.display()}"
        string += f"Overlap area: {self.coaster1.overlap()}\n"
        string += f"Distance needed to shift: {self.coaster1.shift_distance(self.x0)}\n"
        return string

    def run(self):
        self.get_input()
        self.get_newton_input()
        return self.coaster1.get_radius(), self.display_output()


if __name__ == '__main__':

    operation = int(input("Do you want output in JSON or XML? 1 for JSON/0 for XML \n"))

    if operation == 1:
        final_dict = {}
        cheers = CHEERS()
        radius, result = cheers.run()
        final_dict[str(radius)] = str(result)
        print(final_dict)

    elif operation == 0:
        s = 1
        final_dict = {}
        while s != 0:
            cheers = CHEERS()
            radius, result = cheers.run()
            final_dict[str(radius)] = str(result)
            print(final_dict)
            s = int(input("Do you wish to continue?1/0\n"))

        xml = dicttoxml(final_dict)
        xml_decode = xml.decode()
        xmlFile = open("xmlOutput.xml", "w")
        xmlFile.write(xml_decode)
        xmlFile.close()

        names = list(final_dict.keys())
        values = list(final_dict.values())

        plt.bar(range(len(final_dict)), values, tick_label=names)
        plt.show()
