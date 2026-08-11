# ==============================================================================
# LESSON 6: VARIABLES & PRIMITIVE TYPES - CLASSWORK ASSIGNMENT
# ==============================================================================
# INSTRUCTIONS: 
# 1. Uncomment the broken code blocks one by one.
# 2. Fix the variable naming, value assignment, data type, or operation errors.
# 3. Leave concise comments explaining WHY you made your changes.
# ==============================================================================


# ------------------------------------------------------------------------------
# CHALLENGE 1: The Countertop Overflow
# Fix the variable assignment ordering so Python saves the values safely.
# ------------------------------------------------------------------------------

# 12000 = shipping_fee
# "Lagos Warehouse" = delivery_hub

# print(f"Hub: {delivery_hub} | Fee: ₦{shipping_fee}")

shipping_fee = 12000
delivery_hub = "Lagos Warehouse"
print(f"Hub: {delivery_hub} | Fee: ₦{shipping_fee}")

# ------------------------------------------------------------------------------

# CHALLENGE 2: Mathematical Data Disconnect
# Fix the values below so that the discount calculation works without crashing.
# ------------------------------------------------------------------------------

# item_price = "5000"
# discount_amount = "1500"
# # This line will crash if the variables above are left as text strings!
# final_total = item_price - discount_amount
# print(f"Calculated Checkout Total: ₦{final_total}")

item_price = 5000
discount_amount = 1500

# This line will crash if the variables above are left as text strings!
final_total = item_price - discount_amount
print(f"Calculated Checkout Total: ₦{final_total}")




# ------------------------------------------------------------------------------
# CHALLENGE 3: The Illegal Character Search
# Clean up the variable names below so they follow proper Python naming layout.
# ------------------------------------------------------------------------------

# user name = "Amina"
# customer-phone = "08012345678"
# 1st_order_total = 14500.50

# print(f"Customer: {user name} | Contact: {customer-phone} | Due: ₦{1st_order_total}")

user_name = "Amina"
customer_phone = "08012345678" #corrected variable names to use underscores instead of hyphens to follow Python's variable naming convention.
first_order_total = 14500.50 #corrected variable names to use underscores instead of numbers at the beginning to follow Python's variable naming convention.

print(f"Customer: {user_name} | Contact: {customer_phone} | Due: ₦{first_order_total}") # used underscores instead of spaces and hyphens in variable names, and replaced the leading digit with a word to follow Python's variable naming conventions.



# ------------------------------------------------------------------------------
# CHALLENGE 4: Truth or Text Identification
# Fix the logic below so that it displays the data type as <class 'bool'>, 
# and ensure the state is correctly typed.
# ------------------------------------------------------------------------------

# delivery_completed = "False"

# # TODO: Fix the line above so this check actually confirms it is a real boolean
# print(type(delivery_completed))

delivery_completed = False
print(type(delivery_completed)) # corrected the variable assignment to a boolean value instead of a string.


# ------------------------------------------------------------------------------
# CHALLENGE 5: The Floating Point Correction
# A system requires delivery weight to be a float and package count to be an int. 
# Fix the values below so their type checks print exactly <class 'float'> and <class 'int'>.
# ------------------------------------------------------------------------------

# total_weight = "24.5"
# total_packages = 12.0

# print(type(total_weight))    # Must output <class 'float'>
# print(type(total_packages))  # Must output <class 'int'>

total_weight = 24.5 # converted the string to a float
total_packages = 12 #converted the float to an integer

print(type(total_weight))    # Must output <class 'float'>
print(type(total_packages))  # Must output <class 'int'>


# ==============================================================================
# END OF ASSIGNMENT
# When everything prints perfectly with no errors, paste your solution back here!
# ==============================================================================