"""
Lesson 22: Sets and Membership Comparisons Script
"""

# Challenge 1
# Instruction: Correct the set declaration syntax so that the empty container registers as a valid set type in memory instead of collapsing into an empty dictionary
# display_specials_tray = {}
# print(f"Verified Storage Node Profile: {type(display_specials_tray)}")

display_specials_tray = set()               #corrected the set declaration syntax to create an empty set instead of an empty dictionary
print(f"Verified Storage Node Profile: {type(display_specials_tray)}")


# Challenge 2
# Instruction: Correct the lookup line by replacing the broken list-style bracket index with a high-speed boolean membership check to verify if "Cinnamon" is available
# core_toppings = {"Cinnamon", "Cocoa", "Vanilla"}
# extracted_topping = core_toppings[0]
# print(f"Ingredient Verification Confirmation Status: {extracted_topping}")

core_toppings = {"Cinnamon", "Cocoa", "Vanilla"}
if "Cinnamon" in core_toppings:             #checked if "Cinnamon" is in the set
    extracted_topping = True                #set the extracted_topping to True if "Cinnamon" is found
    print(f"Ingredient Verification Confirmation Status: {extracted_topping}")


# Challenge 3
# Instruction: Execute an intersection comparison between the two trays to isolate and display only the premium toppings that both bars have in common
# main_bar_tray = {"Cinnamon", "Cocoa", "Vanilla"}
# island_bar_tray = {"Cocoa", "Nutmeg", "Vanilla"}
# mutual_toppings_grid = main_bar_tray
# print(f"Consolidated Mutual Toppings Track: {mutual_toppings_grid}")

main_bar_tray = {"Cinnamon", "Cocoa", "Vanilla"}
island_bar_tray = {"Cocoa", "Nutmeg", "Vanilla"}
mutual_toppings_grid = main_bar_tray & island_bar_tray          #isolated the premium toppings that both bars have in common using intersection comparison
print(f"Consolidated Mutual Toppings Track: {mutual_toppings_grid}")


# Challenge 4
# Instruction: Refactor the subtraction order so that the difference operation isolates and yields only the toppings unique to main_bar_tray compared to island_bar_tray
# main_bar_tray = {"Cinnamon", "Cocoa", "Vanilla"}
# island_bar_tray = {"Cocoa", "Nutmeg", "Vanilla"}
# unique_toppings_record = island_bar_tray - main_bar_tray
# print(f"Exclusive Main Station Toppings Ledger: {unique_toppings_record}")

main_bar_tray = {"Cinnamon", "Cocoa", "Vanilla"}
island_bar_tray = {"Cocoa", "Nutmeg", "Vanilla"}
unique_toppings_record = main_bar_tray - island_bar_tray            #isolated the toppings unique to main_bar_tray
print(f"Exclusive Main Station Toppings Ledger: {unique_toppings_record}")


# Challenge 5
# Instruction: Based on your research, add the single element "Mint" using the right insertion tool, then merge the backup_stock list elements in-place using the collection update method tool
# active_specials = {"Cinnamon", "Cocoa"}
# backup_stock = ["Nutmeg", "Vanilla-Sugar"]
# print(f"Final Integrated Inventory Matrix: {active_specials}")

active_specials = {"Cinnamon", "Cocoa"}
active_specials.add("Mint")             #added "Mint" to the set
backup_stock = ["Nutmeg", "Vanilla-Sugar"]
active_specials.update(backup_stock)        #merged the backup_stock list elements into the set
print(f"Final Integrated Inventory Matrix: {active_specials}")
