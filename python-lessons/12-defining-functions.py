"""
Lesson 12: Defining Functions Development Script
"""

# Challenge 1
# Instruction: Fix the declaration and tracking flow so that running this script executes the function body and prints the text cleanly
# def log_system_startup():
#     print("Initializing core hardware modules...")
#     print("Coffee cart network automation active.")

def log_system_startup():
    print("Initializing core hardware modules...")
    print("Coffee cart network automation active.")
log_system_startup()        #called the function without arguments since it doesn't need an arguement to run

# Challenge 2
# Instruction: Fix the broken structural design pattern by eliminating the global dependency variable, refactoring the block to use isolated input parameters instead
# def print_receipt_label():
#     print(f"Receipt Log -> Name: {global_customer} | Item: {global_drink}")
# global_customer = "Chidi"
# global_drink = "Espresso"
# print_receipt_label()

def print_receipt_label(global_customer = "Chidi", global_drink = "Espresso"):      #moved the global variables to be parameters of the function with default values
    print(f"Receipt Log -> Name: {global_customer} | Item: {global_drink}")

print_receipt_label()


# Challenge 3
# Instruction: Rectify this calculating module so that the final numeric sum is safely passed back to the outer namespace and printed, instead of disappearing into the void
# def calculate_cart_subtotal(quantity, single_price):
#     subtotal = quantity * single_price

# calculated_checkout = calculate_cart_subtotal(3, 4200.0)
# print(f"Total Amount Due: ₦{calculated_checkout}")

def calculate_cart_subtotal(quantity, single_price):
    subtotal = quantity * single_price
    return subtotal         #returned the function value so that it can be accessible outside the function

calculated_checkout = calculate_cart_subtotal(3, 4200.0)
print(f"Total Amount Due: ₦{calculated_checkout}")


# Challenge 4
# Instruction: Refactor the function declaration line to supply a default fallback parameter of "whole" to milk_type so the custom execution block runs without throwing a TypeError
# def compile_beverage_recipe(base_coffee, milk_type):
#     return f"Brewing {base_coffee} with {milk_type} milk matrix."

# standard_order = compile_beverage_recipe("Mocha")
# print(standard_order)

def compile_beverage_recipe(base_coffee, milk_type="whole"):        #set the value of the second parameter to a default fallback
    return f"Brewing {base_coffee} with {milk_type} milk matrix."

standard_order = compile_beverage_recipe("Mocha")
print(standard_order)


# Challenge 5
# Instruction: Rearrange the statement execution order so that the console prints the success message, updates log_flag, and passes back the completion string cleanly instead of exiting early
# def verify_payment_routing(approval_code):
#     return "Route Verified"
#     print(f"Transaction match confirmed for code: {approval_code}")
#     log_flag = True

# routing_status = verify_payment_routing("AUTH-992")
# print(routing_status)

def verify_payment_routing(approval_code):   #used a default parameter for log_flag to avoid a NameError
    print(f"Transaction match confirmed for code: {approval_code}")
    log_flag = True
    return "Route Verified"     #moved the return statement to the end of the function so that it doesn't exit early and allows the other statements to run
    
routing_status = verify_payment_routing("AUTH-992")
print(routing_status)
