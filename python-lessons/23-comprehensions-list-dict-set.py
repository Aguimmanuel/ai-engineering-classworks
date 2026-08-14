"""
Lesson 23: Data Comprehensions Script
"""

# Challenge 1
# Instruction: Convert the multi-line manual for-loop pipeline below into a single, optimized inline List Comprehension statement
# base_pumps = [1, 2, 3]
# doubled_pumps = []
# for p in base_pumps:
#     doubled_pumps.append(p * 2)
# print(doubled_pumps)
base_pumps = [1, 2, 3]
doubled_pumps = [p * 2 for p in base_pumps]         #use a list comprehension to double the values in base_pumps
print(doubled_pumps)


# Challenge 2
# Instruction: Fix the syntax error inside this list comprehension by adjusting the position of the simple filtering if statement so it sits at the correct boundary end
# orders = ["small", "large", "medium", "large", "small"]
# large_only = [size if size == "large" for size in orders]
# print(large_only)

orders = ["small", "large", "medium", "large", "small"]
large_only = [size for size in orders if size == "large"]       #use a list comprehension to filter large orders
print(large_only)


# Challenge 3
# Instruction: Fix the dictionary comprehension syntax so that it maps keys to modified values using the correct pairing layout, preventing it from collapsing into a set
# menu_whiteboard = {"Latte": 4500.0, "Espresso": 3500.0}
# discounted_menu = {drink for drink, price in menu_whiteboard.items()}
# print(discounted_menu)

menu_whiteboard = {"Latte": 4500.0, "Espresso": 3500.0}
discounted_menu = {drink:price for drink, price in menu_whiteboard.items()}         #use a dictionary comprehension to create a new dictionary with discounted prices
print(discounted_menu)


# Challenge 4
# Instruction: Refactor this list mapping block into a unique Set Comprehension to clean up the data array, automatically stripping white spaces and removing all duplicates in-place
# messy_spices = ["  cinnamon ", "cocoa ", "cinnamon", "nutmeg"]
# clean_spices = messy_spices
# print(clean_spices)

messy_spices = ["  cinnamon ", "cocoa ", "cinnamon", "nutmeg"]
clean_spices = {s.strip() for s in messy_spices}                       #use a strip method to remove whitespace and a set comprehension to remove duplicates
print(clean_spices)


# Challenge 5
# Instruction: Based on your research, build a data mutation comprehension using an inline if/else ternary operator at the front of the statement to transform the cup sizes list: any "large" becomes "Premium", and any other size becomes "Regular"
# cup_sizes = ["small", "large", "medium", "large"]
# classified_station = cup_sizes
# print(classified_station)

cup_sizes = ["small", "large", "medium", "large"]
classified_station = ["Premium" if sizes == "large" else "Regular" for sizes in cup_sizes]              #use a list comprehension to classify cup sizes 
print(classified_station)
