"""
Lesson 20: Tuples and Immutability Script
"""

# Challenge 1
# Instruction: Correct the critical data assignment bug by refactoring the mutable update command so the script reads and prints the recipe safely without attempting a forbidden mutation
# signature_recipe = ("Vanilla", "Caramel", "Hazelnut")
# signature_recipe[1] = "Mocha"
# print(f"Active House Blend Composition: {signature_recipe}")
signature_recipe = ("Vanilla", "Caramel", "Hazelnut")
# signature_recipe[0] = "Mocha"
print(f"Active House Blend Composition: {signature_recipe}")



# Challenge 2
# Instruction: Fix the single-item tuple declaration so that it registers as a valid tuple data type in memory instead of collapsing into a standard primitive string
# limited_edition_syrup = ("Mint")
# print(f"Container Type Verification: {type(limited_edition_syrup)}")
limited_edition_syrup = ("Mint",)                           #added a comma to make it a tuple
print(f"Container Type Verification: {type(limited_edition_syrup)}")



# Challenge 3
# Instruction: Fix the multi-variable data layout on the left side of the assignment operator so that the unpacking sequence executes perfectly without throwing a structural ValueError crash
# telemetry_package = (4.8125, -73.9912, 15.0)
# latitude_coordinate, longitude_coordinate = telemetry_package
# print(f"Unpacked Telemetry Matrices -> Lat: {latitude_coordinate} | Lon: {longitude_coordinate}")
telemetry_package = (4.8125, -73.9912, 15.0)
latitude_coordinate, longitude_coordinate, distance = telemetry_package              #added distance to unpack all values
print(f"Unpacked Telemetry Matrices -> Lat: {latitude_coordinate} | Lon: {longitude_coordinate} | dist: {distance}")



# Challenge 4
# Instruction: Refactor this brittle block by wrapping it inside a defensive try/except block that catches the precise mutation runtime error, printing an organized warning log instead of crashing out
# strict_profile = ("AUTH_KEY", "SECURE_ROUTE")
# strict_profile[0] = "HIJACK_ATTEMPT"
# print(f"Current Profile: {strict_profile}")
strict_profile = ("AUTH_KEY", "SECURE_ROUTE")
try:                                                    #used a try/except block to catch the error
    strict_profile[0] = "HIJACK_ATTEMPT"
except TypeError as e:
    print(f"Caught an error: {e}")
    print(f"Current Profile: {strict_profile}")


# Challenge 5
# Instruction: Demonstrate tuple data science workflow utilities by cleanly unpacking this multi-element dataset inline directly inside the print statement loop header
# dataset_records = [("Sensor_A", 45.2), ("Sensor_B", 50.8)]
# for record in dataset_records:
#     print(f"Node Tag ID: {record} monitors metric limit value: {record}")
dataset_records = [("Sensor_A", 45.2), ("Sensor_B", 50.8)]
for sensor, metric in dataset_records:
    print(f"Node Tag ID: {sensor} monitors metric limit value: {metric}")         #this prints the first and second elements of the tuple in the list
