"""
Lesson 21: Dictionaries and Key Mapping Script
"""

# Challenge 1
# Instruction: Correct the assignment syntax violation inside the curly braces so that the dictionary links keys to values using the right symbol mapping rules
# kiosk_menu = { "Latte" = 4500.0, "Espresso" = 3500.0 }
# print(f"Registered Menu Grid: {kiosk_menu}")

kiosk_menu = { "Latte" : 4500.0, "Espresso" : 3500.0 }          #assignment syntax violation corrected by replacing the equal sign with a colon to properly map keys to values in the dictionary
print(f"Registered Menu Grid: {kiosk_menu}")


# Challenge 2
# Instruction: Correct the lookup line by replacing the list-style index number with the explicit named string key to avoid a runtime KeyError crash
# beverage_catalog = {"Latte": 4500.0, "Espresso": 3500.0}
# current_beverage_rate = beverage_catalog[0]
# print(f"Target Material Price Rate: ₦{current_beverage_rate}")

beverage_catalog = {"Latte": 4500.0, "Espresso": 3500.0}
current_beverage_rate = beverage_catalog["Latte"]             #used the explicit named string keys to retrieve the value for "Latte" from the dictionary
print(f"Target Material Price Rate: ₦{current_beverage_rate}")


# Challenge 3
# Instruction: Fix this tracking code by updating the value of "Latte" to 5000.0, and adding a brand-new menu drink key named "Chai" priced at 4000.0 using bracket assignment notation
# drink_prices = {"Latte": 4500.0, "Espresso": 3500.0}
# print(f"Updated Drink Price Registry: {drink_prices}")

drink_prices = {"Latte": 4500.0, "Espresso": 3500.0}
drink_prices["Latte"] = 5000.0                  #refactored the value of "Latte" to 5000.0
drink_prices["Chai"] = 4000.0                   #added the new menu drink "Chai" with a price of 4000.0
print(f"Updated Drink Price Registry: {drink_prices}")


# Challenge 4
# Instruction: Refactor the brittle bracket lookup by converting it to use the bulletproof .get() method layout supplying a safe fallback default value of 0.0 to prevent an immediate KeyError crash
# shop_register = {"Latte": 4500.0}
# requested_item = "Chai"
# parsed_checkout_rate = shop_register[requested_item]
# print(f"Safe Checkout Processing Value: ₦{parsed_checkout_rate:.2f}")

shop_register = {"Latte": 4500.0}
requested_item = "Chai"
parsed_checkout_rate = shop_register.get(requested_item, 0.0)           #used the .get() method to safely retrieve the value for the requested item, providing a default of 0.0 if the item is not found
print(f"Safe Checkout Processing Value: ₦{parsed_checkout_rate:.2f}")


# Challenge 5
# Instruction: Rectify the dictionary structure layout below to resolve the unhashable type compilation failure caused by utilizing an illegal mutable object format as a key
# secure_access_grid = { ["admin_user", "route_a"]: "GRANTED" }
# print(f"Access Authorization Status Level: {secure_access_grid}")

secure_access_grid = { ("admin_user", "route_a"): "GRANTED" }                    #rectified the dictionary structure by using a tuple key instead of a list
print(f"Access Authorization Status Level: {secure_access_grid}")
