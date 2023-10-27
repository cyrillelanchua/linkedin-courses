###walrus operator
## assignment and condition operator (note the code below is infinite loop because it assigns it again to 5)
# while (x := 5) < 10:
#     print(x)
#     x+=1


## loops until the user input exit
y = 0
while (x := input("what is x ")) != "exit":
    print(x + str(y))
    y += 1


## TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": len(values),
    "total": sum(values),
    "average": sum(values) / len(values),
}

values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
l = len(values)
s = sum(values)
val_data = {"length": l, "total": s, "average": s / l}


##using walrus operator
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l,
}
