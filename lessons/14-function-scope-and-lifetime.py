"""
Lesson 14: Function Scope and Lifetime Script
"""

# Challenge 1
# Instruction: Resolve the NameError crash by using the correct control flow keyword to pass the temporary variable's value back out to the global namespace before its stack frame is destroyed
# def steam_milk_napkin():
#     milk_temperature = 65
#     print(f"Local milk heating metric: {milk_temperature}C")
# final_extracted_temp = steam_milk_napkin()
# print(f"Global Register Audit -> Final Temperature verified at: {final_extracted_temp}C")


def steam_milk_napkin():
    milk_temperature = 65
    print(f"Local milk heating metric: {milk_temperature}C")
    return milk_temperature         #returned the value of the local variable so that it can be accessed outside the function

final_extracted_temp = steam_milk_napkin()
print(f"Global Register Audit -> Final Temperature verified at: {final_extracted_temp}C")



# Challenge 2
# Instruction: Link this local update block directly to the top-level whiteboard price variable so that the change modifies global memory instead of silently generating a shadowed local variable
# whiteboard_price = 4500.0
# def update_shop_whiteboard(new_rate):
#     whiteboard_price = new_rate
#     print(f"Internal calculation frame: ₦{whiteboard_price:.2f}")
# update_shop_whiteboard(5000.0)
# print(f"Global Register Audit -> Public Whiteboard display reads: ₦{whiteboard_price:.2f}")

whiteboard_price = 4500.0

def update_shop_whiteboard(new_rate):
    global whiteboard_price             #used the global keyword to link the local variable to the global namespace
    whiteboard_price = new_rate
    print(f"Internal calculation frame: ₦{whiteboard_price:.2f}")

update_shop_whiteboard(5000.0)
print(f"Global Register Audit -> Public Whiteboard display reads: ₦{whiteboard_price:.2f}")



# Challenge 3
# Instruction: Resolve the UnboundLocalError crash by explicitly linking the function block to the global register total tracking reference
# register_total_sales = 12000.0
# def record_beverage_sale(sale_amount):
#     register_total_sales = register_total_sales + sale_amount
#     print(f"Sale transaction confirmed: ₦{sale_amount:.2f}")
# record_beverage_sale(3500.0)
# print(f"Global Register Audit -> Consolidated terminal balance: ₦{register_total_sales:.2f}")

register_total_sales = 12000.0

def record_beverage_sale(sale_amount):
    global register_total_sales         #used the global keyword to link the local variable to the global namespace
    register_total_sales = register_total_sales + sale_amount
    print(f"Sale transaction confirmed: ₦{sale_amount:.2f}")

record_beverage_sale(3500.0)
print(f"Global Register Audit -> Consolidated terminal balance: ₦{register_total_sales:.2f}")



# Challenge 4
# Instruction: Refactor the nested function call hierarchy by utilizing the correct enclosure keyword so that the inner update block successfully modifies the outer parent function's order tracking variable
# def run_coffee_cart_system():
#     active_cart_order = "Espresso"
#     def alter_active_beverage(target_beverage):
#         active_cart_order = target_beverage
#         print(f"Nested inner routine: Modifying tracking state to {active_cart_order}")
#     alter_active_beverage("Latte")
#     print(f"Outer system scope: Final consolidated cart log reads {active_cart_order}")
# run_coffee_cart_system()

def run_coffee_cart_system():
    active_cart_order = "Espresso"
    
    def alter_active_beverage(target_beverage):
        nonlocal active_cart_order      #used the nonlocal keyword to link the inner function variable to the outer function's variable
        active_cart_order = target_beverage
        print(f"Nested inner routine: Modifying tracking state to {active_cart_order}")
        # return active_cart_order        #returned the modified value
        
    alter_active_beverage("Latte")
    print(f"Outer system scope: Final consolidated cart log reads {active_cart_order}")

run_coffee_cart_system()




# Challenge 5
# Instruction: Fix the critical Built-in scope hijacking vulnerability by renaming the local variable parameter so that it does not blind Python from executing its native print function
# def format_receipt_log(print):
#     system_status = "ONLINE"
#     print(f"Alert Status: {system_status}")
#     print(f"Log Output Payload: {print}")
# format_receipt_log("Transaction Approved Code 200")

def format_receipt_log(print_receipt):  #renamed the local variable to avoid shadowing the built-in print function
    system_status = "ONLINE"
    print(f"Alert Status: {system_status}")
    print(f"Log Output Payload: {print_receipt}")

format_receipt_log("Transaction Approved Code 200")
