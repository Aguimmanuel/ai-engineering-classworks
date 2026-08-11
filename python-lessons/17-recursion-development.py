"""
Lesson 17: Recursion Development Script
"""

import sys      #added the sys module to access system-specific parameters and functions, including recursion limit

# Challenge 1
# Instruction: Resolve the infinite recursion depth crash by implementing a secure base case check at the top that stops execution when mugs hits 0 or less
# def simple_wash_countdown(mugs):
#     print(f"Washing mug number: {mugs}")
#     simple_wash_countdown(mugs - 1)
# simple_wash_countdown(3)
def simple_wash_countdown(mugs):
    if mugs <= 0:               #added a base case check to stop recursion when mugs is 0 or less
        return
    print(f"Washing mug number: {mugs}")
    simple_wash_countdown(mugs - 1)
    return 0

simple_wash_countdown(3)



# Challenge 2
# Instruction: Correct the statement execution order so that the computer evaluates the stop switch condition before diving deeper into the recursive tree
# def recursive_clean_stack(mugs):
#     recursive_clean_stack(mugs - 1)
#     if mugs <= 0:
#         print("All slots sanitized.")
#         return
# recursive_clean_stack(3)
def recursive_clean_stack(mugs):
    if mugs <= 0:
        print("All slots sanitized.")
        return
    recursive_clean_stack(mugs - 1)     #moved the recursive call after the base case check to ensure it evaluates the stop condition first

recursive_clean_stack(3)



# Challenge 3
# Instruction: Fix the recursive reduction argument so that the tracking state actively progresses toward the base case on every iteration step instead of looping statically
# def countdown_counter_mugs(mugs):
#     if mugs <= 0:
#         print("Countdown baseline reached.")
#         return
#     print(f"Mug processing queue position: {mugs}")
#     countdown_counter_mugs(mugs)
# countdown_counter_mugs(3)
def countdown_counter_mugs(mugs):
    if mugs <= 0:
        print("Countdown baseline reached.")
        return
    print(f"Mug processing queue position: {mugs}")
    countdown_counter_mugs(mugs - 1)        #the recursive call now decrements the mugs argument to progress toward the base case

countdown_counter_mugs(3)



# Challenge 4
# Instruction: Refactor the recursive accumulator path so that the function cleanly computes and returns the combined water volume required (15ml per mug) without dropping the mathematical return track
# def calculate_total_wash_water(mugs):
#     if mugs <= 0:
#         return 0
#     # Formula requirement: 15ml for the current mug + volume of the remaining mugs
#     calculate_total_wash_water(mugs - 1)
# total_water_consumed = calculate_total_wash_water(3)
# print(f"Total calculated pipeline water payload: {total_water_consumed}ml")
def calculate_total_wash_water(mugs):
    if mugs <= 0:
        return 0
    # Formula requirement: 15ml for the current mug + volume of the remaining mugs
    return 15 + calculate_total_wash_water(mugs - 1)                    #return the total water consumed for the current mug and the remaining mugs

total_water_consumed = calculate_total_wash_water(3)
print(f"Total calculated pipeline water payload: {total_water_consumed}ml")



# Challenge 5
# Instruction: Import the correct core system module and execute the precise environment query method to output your local VS Code runtime's maximum allowable recursion limit
# Maximum recursion depth limit readout

maximum_allowed_depth = sys.getrecursionlimit()          # used the getrecursionlimit method to get the current recursion limit
print(f"System environment allocation parameter limit: {maximum_allowed_depth}")































#This is a commented-out example of a simple recursive function that prints numbers from 1 to 10. It includes a base case to prevent infinite recursion.
# def printnum(num):
#     if num > 10:
#         return
#     print(num)
#     printnum(num + 1)

# printnum(1)

    




