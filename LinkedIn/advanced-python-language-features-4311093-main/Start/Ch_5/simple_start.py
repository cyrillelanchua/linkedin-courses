# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values
def to_false(x):
    return False


x = True

# TODO: Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case "Zero":
        print("zeor")
    case True:
        print(to_false(x))
    case _:
        print("no value")
