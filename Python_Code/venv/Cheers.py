from Python_Code.venv.Coaster import Coaster
from xml.etree.ElementTree import Element, tostring


class CHEERS:
    def __init__(self):
        self.coaster1 = None

    def get_input(self):
        r1 = float(input("Enter the radius of coaster: "))
        self.coaster1 = Coaster(r1)
        self.x0 = float(input("Enter the starting point for newton method: "))

    def display_output(self):
        string = ""
        string += f"Coaster 1:\n"
        string += f"{self.coaster1.display()}"
        string += f"Overlap area: {self.coaster1.overlap()}\n"
        string += f"Distance needed to shift: {self.coaster1.shift_distance(self.x0)}\n"
        return string

    def run(self):
        self.get_input()
        return self.coaster1.get_radious(), self.display_output()


def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        # create an Element
        # class object
        child = Element(key)
        child.text = str(val)
        elem.append(child)

    return elem

if __name__ == '__main__':
    s = 1
    final_dict = {}
    while (s != 0):
        cheers = CHEERS()
        radius, result = cheers.run()
        final_dict[str(radius)] = str(result)
        print(final_dict)
        s = int(input("Do you wish to continue?1/0\n"))
        print(s)

    e = dict_to_xml('Circle', final_dict)
    print(e)
    print(tostring(e))
