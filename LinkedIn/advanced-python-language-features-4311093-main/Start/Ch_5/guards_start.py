# Example file for Advanced Python: Language Features by Joe Marini
# Using pattern guards to restrict how matches are made


# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius**2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [
    Circle(5),
    Square(4),
    Rectangle(4, 6),
    Square(7),
    Circle(9),
    Rectangle(2, 5),
    Rectangle(5, 5),
]

# use pattern matching to process each shape
# include pattern guards for more detailed processing
for shape in shapes:
    match shape:
        # TODO: add a pattern guard for Circle
        case Circle(radius=r) if r >= 6:
            print(f"Large circle with area {shape.getarea()}")
        case Circle():
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle(width=w, height=h) if h == w:
            print(f"square rectangle with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")

# TODO: Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.upper():
            print(f"{d} is an uppercase string")
        case str():
            print(f"{d} is an NOT uppercase string")
        case bool():
            print(f"this is an {d} bool")
        case int():
            print(f"this ia an int {d}")
        case _:
            print(f"{d}: Something else")

x = [1, 2, 3, 4, 5]
func = lambda y: y + 5 + y * 2
newlist = list(map(lambda y: y * 2, x))
print(newlist)
print(func(24))
