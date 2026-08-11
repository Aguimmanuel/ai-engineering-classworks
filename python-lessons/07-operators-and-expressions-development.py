"""
Lesson 7: Operators and Expressions Development Script
"""

# Challenge 1
# Requirements: Change the output type from float to int
raw_servings = 16
guest_divisor = 4
calculated_servings = raw_servings / guest_divisor
calculated_servings = int(raw_servings / guest_divisor) # converted the float result of the division to an integer using the int() function.

print(calculated_servings)  


# Challenge 2
# Requirements: Must evaluate to 3.75, not 6.0
base_scoops = 3
milk_ounces = 12
average_volume = base_scoops + milk_ounces / 4
average_volume = (base_scoops + milk_ounces) / 4 # added parentheses to ensure that the addition of base_scoops and milk_ounces is performed before the division by 4, resulting in the correct average volume of 3.75.

print(average_volume)  


# Challenge 3
# Requirements: Must evaluate to False (both milk AND cereal must be sufficient)
milk_inventory = 4
cereal_inventory = 1
bowl_available = True
can_serve_breakfast = milk_inventory >= 8 or cereal_inventory >= 3 and bowl_available
can_serve_breakfast = milk_inventory >= 8 and cereal_inventory >= 3 and bowl_available # changed the logical operator from 'or' to 'and' to ensure that both milk_inventory and cereal_inventory must meet their respective thresholds, along with bowl_available being True, for can_serve_breakfast to evaluate to True. This ensures that breakfast can only be served if all conditions are satisfied.
print(can_serve_breakfast)  


# Challenge 4
# Requirements: Must evaluate to True when exact boiling threshold is reached
current_temperature = 100
boiling_threshold = 100
is_boiling = current_temperature > boiling_threshold
is_boiling = current_temperature >= boiling_threshold #
print(is_boiling)  


# Challenge 5
# Requirements: Change the logical operator so that the expression crashes with a ZeroDivisionError instead of short-circuiting to True
is_server_online = True
system_alert_active = is_server_online or (10 / 0 == 0)
system_alert_active = is_server_online and (10 / 0 == 0) #changed the logical operator from 'or' to 'and' to ensure that the second part of the expression (10 / 0 == 0) is evaluated, which will raise a ZeroDivisionError when the code is executed, instead of short-circuiting to True when is_server_online is True.
print(system_alert_active)