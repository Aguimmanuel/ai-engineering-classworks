"""
Lesson 8: Type Casting Development Script
"""

# Challenge 1: Fix the concatenation error so it outputs a mathematical calculation
ordered_bananas = "3"
ordered_milk = "2.5"
# total_units = ordered_bananas + ordered_milk
total_units = int(ordered_bananas) + float(ordered_milk)
print(total_units)  


# Challenge 2: Prevent the ValueError crash caused by parsing this string format
measured_liters = "1.75"
# integer_cast_check = int(measured_liters)
integer_cast_check = float(measured_liters)
print(integer_cast_check)  


# # Challenge 3: Resolve the TypeError crash when connecting these values
# completed_smoothies = 4
# summary_message = "Smoothies successfully processed: " + completed_smoothies
# print(summary_message)  


# # Challenge 4: Apply validation logic so this script sets a fallback value instead of crashing
# unverified_input = "smoothie"
# safe_numeric_assignment = int(unverified_input)
# print(safe_numeric_assignment)  


# # Challenge 5: Format the final output to print as a whole number string ("15") instead of a decimal string
# raw_count = 15.0
# final_output = str(raw_count)
# print(final_output)  
