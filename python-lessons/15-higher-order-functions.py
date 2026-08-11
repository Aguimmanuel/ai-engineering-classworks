"""
Lesson 15: Higher Order Functions Script
"""

# Challenge 1
# Instruction: Open the lazy generator object by wrapping the expression in the correct data container casting tool so that it prints a real value list instead of a hex address
# menu_prices = [3500.0, 4200.0, 5000.0]
# updated_prices = map(lambda price: price + 500.0, menu_prices)
# print(updated_prices)
menu_prices = [3500.0, 4200.0, 5000.0]
updated_prices = map(lambda price: price + 500.0, menu_prices)
print(list(updated_prices))     #modified the print statement to cast the map object to a list so that it prints the actual values instead of a memory address



# Challenge 2
# Instruction: Correct the lambda syntax inside this filtration block so that it accurately isolates and displays only drinks that cost 4000.0 or less
# chalkboard_menu = [
#     {"name": "Espresso", "price": 3500.0},
#     {"name": "Latte", "price": 4500.0},
#     {"name": "Mocha", "price": 5000.0}
# ]
# budget_options = list(filter(chalkboard_menu, lambda item: item["price"] <= 4000.0))
# print(budget_options)
chalkboard_menu = [
    {"name": "Espresso", "price": 3500.0},
    {"name": "Latte", "price": 4500.0},
    {"name": "Mocha", "price": 5000.0}
]
budget_options = list(filter(lambda x: x["price"] <= 4000.0, chalkboard_menu)) #corrected the order of the parameters in the filter function, placing the lambda function first and the list second
print(budget_options)


# Challenge 3
# Instruction: Provide the missing target parameter check on the sorting invocation so that Python knows to look inside the dictionaries and organize them cleanly by price
# beverage_catalog = [
#     {"name": "Mocha", "price": 5000.0},
#     {"name": "Espresso", "price": 3500.0},
#     {"name": "Latte", "price": 4500.0}
# ]
# sorted_catalog = sorted(beverage_catalog)
# print(sorted_catalog)
beverage_catalog = [
    {"name": "Mocha", "price": 5000.0},
    {"name": "Espresso", "price": 3500.0},
    {"name": "Latte", "price": 4500.0}
]
sorted_catalog = sorted(beverage_catalog, key=lambda x: x["price"]) #added the key parameter to the sorted function, specifying that the sorting should be based on the "price" key in each dictionary
print(sorted_catalog)


# Challenge 4
# Instruction: Clean up the syntax by refactoring this functional map-lambda chain into a sleek, pythonic List Comprehension that produces identical mathematical data outcomes
# base_counts = [10, 20, 30]
# scaled_counts = list(map(lambda x: x * 3, base_counts))
# print(scaled_counts)
 
base_counts = [10, 20, 30]
scaled_counts = [x * 3 for x in base_counts] #refactored the map-lambda chain into a list comprehension
print(scaled_counts)


# Challenge 5
# Instruction: Correct the broken map lambda so that it correctly mutates the price metric while passing back the rest of the object layout, preventing it from dropping names and converting to raw numbers
# raw_inventory = [
#     {"name": "Cup", "count": 10},
#     {"name": "Spoon", "count": 5}
# ]
# updated_inventory = list(map(lambda item: item["count"] + 2, raw_inventory))
# print(updated_inventory)

raw_inventory = [
    {"name": "Cup", "count": 10},
    {"name": "Spoon", "count": 5}
]
updated_inventory = list(map(lambda item: {"name": item["name"], "count": item["count"] + 2}, raw_inventory))
print(updated_inventory)





















































# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = map(lambda x: x * x, numbers)
# print(list(result))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))

# numbers = [{'name': 'Elice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
# result = sorted(numbers, key=lambda x: x['name'])
# print(list(result))

# numbers = [('Elice', 30), ('Bob', 25), ('Charlie', 35)]
# result = sorted(numbers, key=lambda x: x[1])
# print(result)

# numbers = [13, 12, 5, 4, 25, 16, 7, 78, 9, 10]
# result = sorted(numbers)
# print(result)