"""
Lesson 8: Type Casting Development Script
"""

# Challenge 1: Fix the concatenation error so it outputs a mathematical calculation
ordered_bananas = "3"
ordered_milk = "2.5"
# total_units = ordered_bananas + ordered_milk
total_units = int(ordered_bananas) + float(ordered_milk) # convert the string values to the correct datatype using int() and float() respectively
print(total_units)  


# Challenge 2: Prevent the ValueError crash caused by parsing this string format
measured_liters = "1.75"
# integer_cast_check = int(measured_liters)
integer_cast_check = float(measured_liters) # convert to float using the float() method
print(integer_cast_check)  


# # Challenge 3: Resolve the TypeError crash when connecting these values
completed_smoothies = 4
# summary_message = "Smoothies successfully processed: " + completed_smoothies
summary_message = "Smoothies successfully processed: " + str(completed_smoothies) # convert to string using the str() method
print(summary_message)  


# # Challenge 4: Apply validation logic so this script sets a fallback value instead of crashing
unverified_input = "smoothie"
# safe_numeric_assignment = int(unverified_input)
try:                                                   # Use the try and except method to handle any potential crash
    safe_numeric_assignment = int(unverified_input)
except ValueError:
    safe_numeric_assignment = 0
print(safe_numeric_assignment)  


# # Challenge 5: Format the final output to print as a whole number string ("15") instead of a decimal string
raw_count = 15.0
# final_output = str(raw_count)
final_output = str(int(raw_count))       #convert the string to integer with the int() function then back to string with the str() function as required by the challenge 
print(final_output)  
