"""
Lesson 9: Control Flow Conditionals Script
"""

# # Challenge 1: Fix the indentation structure so the program executes cleanly without crashing
# current_mode = "manual"
# if current_mode == "manual":
# print("Manual mode activated")
# print("Overriding automatic target settings")

current_mode = "manual"
if current_mode == "manual":
    print("Manual mode activated") #fixed indentation to ensure the print statement is executed when the condition is true
    print("Overriding automatic target settings")


# # Challenge 2: Refactor these independent blocks to a single connected conditional chain to prevent the variable from being overwritten
# kettle_selection = "Green Tea"
# heat_setting = 0
# if kettle_selection == "Green Tea":
#     heat_setting = 80
# if kettle_selection != "Coffee":
#     heat_setting = 100
# print(heat_setting)

kettle_selection = "Green Tea"
heat_setting = 0
if kettle_selection == "Green Tea":
    heat_setting = 80
elif kettle_selection != "Coffee":  #changed the if statement to elif to handle the every kettle_selection other than "Green Tea" or "Coffee" 
    heat_setting = 100
print(heat_setting)


# # Challenge 3: Replace the assignment bug with a valid comparison check
# kettle_power_on = True
# if kettle_power_on = True:
#     print("System active")

kettle_power_on = True
if kettle_power_on == True: #comparison operator is used for conditional statement not the assignment operator
    print("System active")


# # Challenge 4: Implement a catch-all safety logic block that flags any unknown beverage orders as "unsupported"
# ordered_beverage = "Herbal Blend"
# beverage_status = "Processing"
# if ordered_beverage == "Green Tea":
#     beverage_status = "80C optimization applied"
# elif ordered_beverage == "Coffee":
#     beverage_status = "90C optimization applied"
# print(beverage_status)

ordered_beverage = "Herbal Blend"
beverage_status = "Processing"
if ordered_beverage == "Green Tea":
    beverage_status = "80C optimization applied"
elif ordered_beverage == "Coffee":
    beverage_status = "90C optimization applied"
else:                                             # used else to handle all other conditions where an unknown beverage order is not supported
    beverage_status = "unsupported"
print(beverage_status)


# # Challenge 5: Adjust the scoping so that the completion statement runs globally, while the warning statement stays contained
# water_temp = 105
# if water_temp > 100:
#     print("Warning: Critical boiling threshold exceeded!")
#     print("Emergency system shutdown complete.")
#     print("Kettle diagnostic execution finished.")

water_temp = 105
if water_temp > 100:
    print("Warning: Critical boiling threshold exceeded!")
    print("Emergency system shutdown complete.")
print("Kettle diagnostic execution finished.")      # completion statements now runs globally while warning statement remains contained in the conditional statement
