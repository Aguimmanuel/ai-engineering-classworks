"""
Lesson 13: Functions and Parameters Script
"""

# Challenge 1
# Instruction: Correct the function call so that it passes arguments in the exact positional sequence order expected by the parameters
# def print_cart_label(customer_name, beverage_item, container_size):
#     print(f"Cup Print -> Name: {customer_name} | Drink: {beverage_item} | Size: {container_size}")
# print_cart_label("large", "Latte", "Alice")

def print_cart_label(customer_name, beverage_item, container_size):
    print(f"Cup Print -> Name: {customer_name} | Drink: {beverage_item} | Size: {container_size}")

print_cart_label("Alice", "Latte", "large") # corrected the positional sequence of the arguments to match the parameter order in the function definition



# Challenge 2
# Instruction: Refactor the function call using explicit keyword arguments so that the data maps correctly despite being completely out of sequential order
# def log_kiosk_receipt(customer, item, price):
#     print(f"Receipt for {customer}: 1x {item} — ₦{price:.2f}")
# log_kiosk_receipt(4500.0, "Chidi", "Cappuccino")

def log_kiosk_receipt(customer, item, price): 
    print(f"Receipt for {customer}: 1x {item} — ₦{price:.2f}")

log_kiosk_receipt(price=4500.0, customer="Chidi", item="Cappuccino") #refactored the function call to use keyword arguments to ensure correct mapping of data


# Challenge 3
# Instruction: Rearrange the parameter order on the function definition line to resolve the structural compile crash caused by bad parameter grouping hierarchy
# def customize_milk_base(milk_option="whole", beverage_base):
#     return f"Processing standard {beverage_base} with {milk_option} base layout."
# processed_recipe = customize_milk_base(beverage_base="Espresso")
# print(processed_recipe)

def customize_milk_base(beverage_base, milk_option="whole"): #rearranged the parameter order so that the default parameter comes after the required parameter
    return f"Processing standard {beverage_base} with {milk_option} base layout."

processed_recipe = customize_milk_base(beverage_base="Espresso")
print(processed_recipe)


# Challenge 4
# Instruction: Fix the function invocation line to eliminate the syntax crash caused by bad sequencing of positional and keyword entries
# def finalize_order_specs(drink, size, milk="whole"):
#     print(f"Final Spec Matrix: {size} {drink} using {milk} milk.")
# finalize_order_specs(drink="Macchiato", "small")

def finalize_order_specs(drink, size, milk="whole"):
    print(f"Final Spec Matrix: {size} {drink} using {milk} milk.")

finalize_order_specs(drink="Macchiato", size="small") #used keyword arguments for both parameters to avoid the syntax error


# Challenge 5
# Instruction: Refactor the function parameter and loop body to utilize the *args syntax so it can dynamically swallow and print any number of arbitrary toppings passed during invocation
# def apply_beverage_toppings(topping_1, topping_2, topping_3):
#     print("Applying structural extra layers:")
#     print(f" - {topping_1}")
#     print(f" - {topping_2}")
#     print(f" - {topping_3}")
# apply_beverage_toppings("cinnamon", "whipped cream", "caramel drizzle", "chocolate flakes")

def apply_beverage_toppings(*topping): #used *args to allow for any number of toppings to be passed
    print("Applying structural extra layers:")
    for top in topping:
        print(f" - {top}")

apply_beverage_toppings("cinnamon", "whipped cream", "caramel drizzle", "chocolate flakes") 