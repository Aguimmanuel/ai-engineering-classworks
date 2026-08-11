# ==============================================================================
# LESSON 5: PYTHON KEYWORDS & SYNTAX - CLASSWORK ASSIGNMENT
# ==============================================================================
# INSTRUCTIONS: 
# 1. Uncomment the broken code blocks one by one.
# 2. Fix the keyword, syntax, indentation, and namespace errors.
# 3. Leave good comments explaining WHY you made your changes.
# ==============================================================================


# ------------------------------------------------------------------------------
# CHALLENGE 1: The Keyword Clash
# Fix this block so that data saves without using protected Python keywords.
# ------------------------------------------------------------------------------

# while = "Morning Batch"
# def = 88
# return = "Room 3A"
# print(f"Class Check-in: {while} | Students: {def} | Lab: {return}")

class_check_in = "Morning Batch"
students_present = 88
lab_number = "Room 3A"
print(f"Class Check-in: {class_check_in} | Students: {students_present} | Lab: {lab_number}") # used descriptive variable names instead of reserved keywords to avoid syntax errors and improve code readability.



# ------------------------------------------------------------------------------
# CHALLENGE 2: The Block Alignment
# This conditional logic has broken formatting. Fix the indentation and colons
# so Python can properly map out the execution blocks.
# ------------------------------------------------------------------------------

# account_balance = 75000
# withdrawal_amount = 20000

# if account_balance >= withdrawal_amount
#     account_balance = account_balance - withdrawal_amount
#     print("Withdrawal successful!")
#       print(f"Remaining balance: ₦{account_balance}")
# else
# print("Insufficient funds available.")

account_balance = 75000
withdrawal_amount = 20000

if account_balance >= withdrawal_amount: #added missing colon to the if statement for proper block execution.
    account_balance = account_balance - withdrawal_amount
    print("Withdrawal successful!")
    print(f"Remaining balance: ₦{account_balance}") # corrected indentation
else: # added missing colon to the else statement for proper block execution.
    print("Insufficient funds available.") # corrected indentation




# ------------------------------------------------------------------------------
# CHALLENGE 3: The Broken Function Tracing
# A function is structured incorrectly below. Correct all structure bugs 
# so the script successfully prints the product status.
# ------------------------------------------------------------------------------

# def verify_stock(quantity)
# if quantity == 0:
#     return "Out of stock"
#     else:
#         return "Items available"

# status = verify_stock(12)
# print(f"Inventory Status: {status}")

def verify_stock(quantity): # added missing colon to the function definition for proper block execution.
    if quantity == 0: # fixed indentation.
        return "Out of stock" 
    else: # fixed indentation and removed unnecessary indentation to align with the if statement.
        return "Items available" #fixed indentation to align with the else statement.

status = verify_stock(12)
print(f"Inventory Status: {status}")


# ------------------------------------------------------------------------------
# CHALLENGE 4: String and Parentheses Closure
# This script has text matching errors and missing structural closures. 
# Fix it so the output displays cleanly.
# ------------------------------------------------------------------------------

# student_name = "Chidi'
# course_title = 'Intro to Programming"

# print("Enrolling student...   
# print(f"Successfully added {student_name} to {course_title}"

student_name = "Chidi" # fixed the string closure by changing the single quote to a double quote.
course_title = "Intro to Programming" # fixed the string closure by changing the single quote to a double quote.

print("Enrolling student...") # fixed the missing closing parenthesis and added a closing quote to the string.
print(f"Successfully added {student_name} to {course_title}") #fixed the missing closing parenthesis and added a closing quote to the string.

# ------------------------------------------------------------------------------
# CHALLENGE 5: Safe Global Namespace Coding
# This code assigns a string value to a built-in tool name. 
# Fix the script so it safely logs the system report without crashing.
# ------------------------------------------------------------------------------

# print = "System Override Active"
# system_status = "Online"

# print(f"Alert: {print}")
# print(f"Main Core Engine Status: {system_status}")

print_value = "System Override Active" # changed the variable name from 'print' to 'print_value' to avoid overwriting the built-in print function, which would cause a crash when trying to use print() later in the code.
system_status = "Online"

print(f"Alert: {print_value}") # changed the variable name from 'print' to 'print_value' in the f-string to correctly reference the new variable name and avoid confusion with the built-in print function.
print(f"Main Core Engine Status: {system_status}") 

# ==============================================================================
# END OF ASSIGNMENT
# When everything prints perfectly with no errors, paste your solution back here!
# ==============================================================================
