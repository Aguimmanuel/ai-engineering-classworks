"""
Lesson 11: Strings and String Manipulation Script
"""

# Challenge 1: Fix the script so that the whitespace trimming and casing operations are permanently saved to the variable
# raw_customer = "  EmEka   "
# raw_customer.strip().capitalize()
# print(f"Verified Name: [{raw_customer}]")

raw_customer = "  EmEka   "
raw_customer = raw_customer.strip().capitalize() #reassigned the variable to the new value
print(f"Verified Name: [{raw_customer}]")



# Challenge 2: Refactor the upper boundary index so that the code correctly extracts the shorthand label "Cap" from the string
# drink_item = "Cappuccino"
# shorthand_code = drink_item[0:2]
# print(shorthand_code)
drink_item = "Cappuccino"
shorthand_code = drink_item[0:3] #corrected the iteration to extract Cap
print(shorthand_code)


# Challenge 3: Fix the manual concatenation crash by refactoring the expression to use a single clean f-string with 2-decimal precision
# beverage_name = "Latte"
# beverage_price = 3500.0
# receipt_log = "Order item: " + beverage_name + " costing ₦" + beverage_price
# print(receipt_log)
beverage_name = "Latte"
beverage_price = 3500.0
receipt_log = f'Order item: {beverage_name}\nCosting: ₦{beverage_price:.2f}' #used the shorthand for decimal precision and moved Costing to a new line to appear cleanly
print(receipt_log)


# Challenge 4: Apply the appropriate parameter constraint to stop the fragmentation sequence right after isolating the primary order token
# order_log = "Mocha with extra cream and sugar and ice"
# tokenized_items = order_log.split(" with ")
# print(tokenized_items)
order_log = "Mocha with extra cream and sugar and ice"
tokenized_items = order_log.split(" with ", maxsplit=1) #used the maxsplit=1 keyword to stop the fragmentation right after getting the primary order
print(tokenized_items)


# Challenge 5: Merge this ingredients data structure back into a singular text layout with a comma-and-space divider separating them
# clean_ingredients = ["espresso shot", "steamed milk", "vanilla syrup"]
# recipe_label = clean_ingredients
# print(f"Recipe Breakdown: {recipe_label}")
clean_ingredients = ["espresso shot", "steamed milk", "vanilla syrup"]
recipe_label = ", ".join(clean_ingredients)     #used the .join method to join the list and turn it to a string
print(f"Recipe Breakdown: {recipe_label}")

