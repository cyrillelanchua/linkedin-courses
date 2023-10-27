# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class
from enum import Enum, unique, auto

GLOBAL = 3


# TODO: enums have human-readable values and types
@unique  # decorator in enum to prevent duplicate values
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # duplicate = 4
    pear = auto()


# TODO: enums have name and value properties
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
# TODO: print the auto-generated value
print(Fruit.pear)
print(type(Fruit.pear))
print(repr(Fruit.pear))
# TODO: enums are hashable - can be used as keys
my_fruits = {}
my_fruits[Fruit.APPLE] = "valie"
print(my_fruits[Fruit.APPLE])
