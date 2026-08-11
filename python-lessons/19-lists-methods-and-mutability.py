"""
Lesson 19: Lists Methods and Mutability Script
"""

# Challenge 1
# Instruction: Fix the assignment trap line so that the new flavor is added cleanly to the end of the list without wiping out the flavors variable container
# syrup_inventory = ["Vanilla", "Caramel", "Hazelnut"]
# syrup_inventory = syrup_inventory.append("Mint")
# print(f"Updated Storage Shelf Log: {syrup_inventory}")
syrup_inventory = ["Vanilla", "Caramel", "Hazelnut"]
syrup_inventory.append("Mint")                          #assigning the result of append() to syrup_inventory was incorrect because append() modifies the list in place and returns None. The correct approach is to call append() without assignment.
print(f"Updated Storage Shelf Log: {syrup_inventory}")


# Challenge 2
# Instruction: Correct the value lookup swap line by using the appropriate method tool that accepts an integer coordinate parameter instead of a literal value name
# flavor_rack = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]
# # Goal: Remove the item at slot 2 ("Hazelnut") and print it
# extracted_flavor = flavor_rack.remove(2)
# print(f"Extracted Production Material: {extracted_flavor}")
# print(f"Remaining Rack Configuration: {flavor_rack}")
flavor_rack = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]
# Goal: Remove the item at slot 2 ("Hazelnut") and print it
extracted_flavor = flavor_rack.pop(2)                                  #use the pop() method with an index to remove and return the item at that position
print(f"Extracted Production Material: {extracted_flavor}")
print(f"Remaining Rack Configuration: {flavor_rack}")


# Challenge 3
# Instruction: Add a defensive validation check to wrap this removal sequence so that the program logs a warning instead of crashing with a ValueError if the item is missing
# syrup_shelf = ["Vanilla", "Caramel"]
# target_removal = "Mocha"
# syrup_shelf.remove(target_removal)
# print(f"Post Cleanup Inventory State: {syrup_shelf}")
syrup_shelf = ["Vanilla", "Caramel"]
target_removal = "Mocha"
try:                                               #use try/except to handle the ValueError so the program doesn't crash if the item is not found in the list
    syrup_shelf.remove(target_removal)
    print(f"Post Cleanup Inventory State: {syrup_shelf}")
except ValueError:
    print("Not a valid syrup list")



# Challenge 4
# Instruction: Fix the assignment bug on the sorting line so that the list organizes itself alphabetically in-place without returning a None value
# chaotic_flavors = ["Mocha", "Vanilla", "Caramel", "Mint"]
# chaotic_flavors = chaotic_flavors.sort()
# print(f"Aligned Display Layout: {chaotic_flavors}") 
chaotic_flavors = ["Mocha", "Vanilla", "Caramel", "Mint"]
chaotic_flavors.sort()                              #sort the list in place without assigning it to a variable, as sort() returns None
print(f"Aligned Display Layout: {chaotic_flavors}") 



# Challenge 5
# Instruction: Based on your research, refactor the code to use the correct built-in function that generates a sorted copy, leaving the original array order completely untouched
# historical_log = ["Mocha", "Espresso", "Latte"]
# # Goal: Create a sorted copy inside dynamic_display, but keep historical_log exactly as it is
# historical_log.sort()
# dynamic_display = historical_log
# print(f"Dynamic Workspace View (Sorted): {dynamic_display}")
# print(f"Historical Archive Entry (Original): {historical_log}")
historical_log = ["Mocha", "Espresso", "Latte"]
# Goal: Create a sorted copy inside dynamic_display, but keep historical_log exactly as it is
dynamic_display = sorted(historical_log)                    #using the sorted() function to create a new sorted list without modifying the original historical_log
print(f"Dynamic Workspace View (Sorted): {dynamic_display}")
print(f"Historical Archive Entry (Original): {historical_log}")
