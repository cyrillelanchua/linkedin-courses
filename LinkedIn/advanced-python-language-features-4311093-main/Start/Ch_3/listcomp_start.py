# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
even_squared = list(
    map(lambda t: t**2, filter(lambda t: t > 4 and t < 16, evens))
)
even_filtered = list(filter(lambda t: t < 100, evens))
print(even_squared)
print(even_filtered)
# TODO: Derive a new list of numbers frm a given list
even_squared = list(e**2 for e in evens if e > 4 and e < 16)
even_filtered = list(e for e in evens if e < 100)
print(even_squared)
print(even_filtered)
# TODO: Limit the items operated on with a predicate condition
