"""
Lesson 18: Lists Creation, Indexing, and Slicing Script
"""

# Challenge 1
# Instruction: Correct the 1-based indexing error so that the variable captures the very first element ("Vanilla") off the list array rack
# syrup_rack = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
# selected_syrup = syrup_rack[1]
# print(f"Target Selection Slot: {selected_syrup}")
syrup_rack = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
selected_syrup = syrup_rack[0]      #
print(f"Target Selection Slot: {selected_syrup}")



# Challenge 2
# Instruction: Refactor the upper boundary index slice coordinates so that the subset slice extracts "Caramel" and "Hazelnut" cleanly without dropping the second item
# flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
#  cocoa_station_set = flavors[1:2]
# print(f"Cocoa Processing Set: {cocoa_station_set}")
flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
cocoa_station_set = flavors[1:3]            #
print(f"Cocoa Processing Set: {cocoa_station_set}")



# Challenge 3
# Instruction: Implement a defensive validation guard clause check using len() to safely assign "Empty Slot" to raw_extraction if the target index is out of bounds, preventing an IndexError crash
# inventory = ["Vanilla", "Caramel"]
# target_index = 2
# raw_extraction = inventory[target_index]
# print(f"Retrieved Inventory Element: {raw_extraction}")
inventory = ["Vanilla", "Caramel"]
target_index = -1
if 0 <= target_index < len(inventory):      #safely checking if the target index is within the valid range of the inventory list to prevent IndexError
    raw_extraction = inventory[target_index]
else:
    raw_extraction = "Empty Slot"
print(f"Retrieved Inventory Element: {raw_extraction}")


# Challenge 4
# Instruction: Refactor the extended slicing parameters using your step stride research to isolate and extract every second item sequentially from the base list array
# bulk_syrups = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint", "Cinnamon"]
# alternating_menu = bulk_syrups[0:5]
# print(f"Alternating Menu Traversal: {alternating_menu}")
bulk_syrups = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint", "Cinnamon"]
alternating_menu = bulk_syrups[::2]             #using a step stride of 2 to extract every second item from the list
print(f"Alternating Menu Traversal: {alternating_menu}")


# Challenge 5
# Instruction: Use the negative stride reversal slicing shortcut to print the entire syrup list upside down from the rear end forward on a single line of calculation
# base_syrups = ["Vanilla", "Caramel", "Hazelnut"]
# reversed_order_list = base_syrups
# print(f"Reversed Layout Track: {reversed_order_list}")
base_syrups = ["Vanilla", "Caramel", "Hazelnut"]
reversed_order_list = base_syrups[::-1]             #using a negative stride of -1 to reverse the list order
print(f"Reversed Layout Track: {reversed_order_list}")
