# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Structural Pattern Matching

# Dry Clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same day service adds 10.00 per same-day item
# Wash and Fold: [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type, dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

test_orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True],
    ],
    [["dress", "M", False, True], ["whites", 5.25], ["darks", 12.5]],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True],
    ],
]

# TODO: process each order
for orders in test_orders:
    price = 0.00
    print("------------------")
    for order in orders:
        match order:
            case garmet, size, True, False:  # CAN JUST BE ONE CASE FOR DRY CLEAN
                price += 14.95
                print(f"Dry Clean:({size}) {garmet} Starched")
            case garmet, size, False, True:
                price += 22.95
                print(f"Dry Clean:({size}) {garmet} same-day")
            case garmet, size, True, True:
                price += 24.95
                print(f"Dry Clean:({size}) {garmet} Starched same-day")
            case garmet, size, False, False:
                price += 12.95
                print(f"Dry Clean:({size}) {garmet}")
            case type, True, size:
                price += 25.00
                print(f"Blanket:({size}) {type} Dry clean")
            case type, False, size:
                price += 25.00
                print(f"Blanket:({size}) {type}")
            case "shirts and jeans" | "whites" | "darks" as description, weight:
                price += (
                    (4.95 * weight)
                    if weight < 15.00
                    else (4.95 * weight * 0.9)
                )
                print(f"Wash/ Fold:{description} weight: {weight}")
    print(f"Order total: {price:.2f}")
    print("------------------")
x = True
y = False

print(
    f"the apple does not faill ffrom the",
    "tree" if x == True else "wood",
    " and ",
    "swamp" if y == True else "jungle ",
)
