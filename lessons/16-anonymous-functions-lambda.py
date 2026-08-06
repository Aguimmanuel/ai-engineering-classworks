"""
Lesson 16: Anonymous Functions (Lambda) Script
"""

# Challenge 1
# Instruction: Resolve the syntax crash by removing the explicitly written keyword that violates the lambda inline parsing layout rules
# scale_syrup = lambda ml: return ml / 30.0
# print(scale_syrup(60.0))

scale_syrup = lambda ml: ml / 30.0      #removed the explicit return keyword which is not supported in lambda function
print(scale_syrup(60.0))


# Challenge 2
# Instruction: Refactor the multiline function call loop structure into a sleek anonymous lambda passed directly inside the map tool to eliminate the named clutter from the namespace
# def multiply_by_five(x):
#     return x * 5
# numbers = [1, 2, 3]
# scaled_numbers = list(map(multiply_by_five, numbers))
# print(scaled_numbers)

numbers = [1, 2, 3]
scaled_numbers = list(map(lambda x: x * 5, numbers)) #removed the custom multiline function and replace it with a simple inline lambda function
print(scaled_numbers)


# Challenge 3
# Instruction: Refactor the multi-line conditional statement below into a single-line ternary expression contained inside a valid lambda structure
# def evaluate_syrup_level(ounces):
#     if ounces >= 16:
#         return "large"
#     else:
#         return "small"
# print(evaluate_syrup_level(12))
    
print((lambda ounces: "large" if ounces >= 16 else "small")(12)) #replaced the multiline custom function with a single-line valid lambda function ternary expression


# Challenge 4
# Instruction: Fix the function invocation down on the print line so that the script actually executes the lambda expression with the input value instead of displaying its raw memory hex address
# calculate_tax = lambda rate: rate * 0.05
# print(calculate_tax)

calculate_tax = lambda rate: rate * 0.05
print(calculate_tax(0.05))      #called the function from the variable assigned to it and passed in the argument


# Challenge 5
# Instruction: Correct the parameter binding architecture so that the anonymous lambda handles multiple distinct input variables cleanly on a single line of calculation
# compute_volume = lambda base, height: base + height * depth
# print(compute_volume(10, 5, 2))

compute_volume = lambda base, height, depth: base + height * depth  #declared the depth parameter first before using it in the math operation
print(compute_volume(10, 5, 2))
