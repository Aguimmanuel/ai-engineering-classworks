"""
Lesson 10: Control Flow Loops Script
"""

# Challenge 1: Fix the repetitive manual print code by converting it into a clean count-controlled loop structure
# print("Twisting spice mill... Step 1")
# print("Twisting spice mill... Step 2")
# print("Twisting spice mill... Step 3")
for i in range(3):                        #used for loop and range() since i already know how many times i want to print the message
    i = i + 1
    print(f"Twisting spice mill... Step {i}")

# Challenge 2: Fix the infinite loop logic bug by ensuring the loop condition can eventually evaluate to False
# current_weight = 0.0
# target_weight = 1.5
# while current_weight < target_weight:
#     print("Grinding...")

current_weight = 0.0
target_weight = 1.5
while current_weight < target_weight:
    print("Grinding...")
    current_weight = current_weight + 0.5   #Accumulates weight naturally until 1.5 is met 



# Challenge 3: Fix the structural design flaw where the tracking variable is reset incorrectly, causing an infinite loop
# while current_weight < 3.0:
#     current_weight = 0.0
#     current_weight = current_weight + 1.0
# print("Target weight confirmed.")

current_weight = 0.0                # moved the variable declaration outside the loop
while current_weight < 3.0:
    current_weight = current_weight + 1.0
print("Target weight confirmed.")


# Challenge 4: Implement an emergency exit safety switch inside this loop that instantly kills the process if temperature spikes above 85 degrees
# kettle_temperature = 70
# while kettle_temperature < 100:
#     kettle_temperature = kettle_temperature + 5
#     print(f"Current Temperature: {kettle_temperature}C")

kettle_temperature = 70
while kettle_temperature < 100:
    kettle_temperature = kettle_temperature + 5

    if kettle_temperature > 85:
        print("CRITICAL LIMIT: Safety termination.")
        break
    print(f"Current Temperature: {kettle_temperature}C")


# Challenge 5: Implement a skip control statement that passes over step number 3 completely, while printing all other steps in the sequence cleanly
# for current_step in range(5):
#     step_display = current_step + 1
#     print(f"Processing step: {step_display}")

for current_step in range(5):
    step_display = current_step + 1
    if step_display == 3:
        continue
    print(f"Processing step: {step_display}")
