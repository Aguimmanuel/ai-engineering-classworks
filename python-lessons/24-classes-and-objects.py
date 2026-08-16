"""
Lesson 24: Classes and Objects Script
"""


# Challenge 1
# Instruction: Fix the constructor declaration signature block below to resolve the
# positional argument TypeError crash by adding the missing tracking reference parameter
class CardboardCup:
    # Constructor block missing a vital positional pointer
    def __init__(self, size, owner):  # added the missing tracking reference parameter 'self' to fix the constructor declaration signature block
        self.size = size
        self.owner = owner
        self.contents = "empty"


# Trigger compilation instantiation test
try:
    alice_cup = CardboardCup("Large", "Alice")
    print(f"Stamping Success -> Owner: {alice_cup.owner}")
except TypeError as e:
    print(f"Compilation Failure Logged: {e}")


# Challenge 2
# Instruction: Fix the spelling execution violation on the special initializer method
# line so that the constructor fires automatically upon object instantiation
class AutomatedKiosk:
    # Incorrect underscore boundary layout
    def __init__(self, location_node):  #used the dunder method __init__ to fix the spelling execution violation
        self.location_node = location_node
        self.status = "ONLINE"


test_kiosk = AutomatedKiosk("Main_Cart_01")
try:
    print(f"Kiosk System Status Node: {test_kiosk.status}")
except AttributeError as e:
    print(f"Initialization Defect Logged: {e}")


# Challenge 3
# Instruction: Correct the data mapping pipeline so that the name "Bob"
# is written using dot notation onto the individual physical stamped
# object instead of corrupting the master class template
class RetailOrderCup:
    def __init__(self, size):
        self.size = size
        self.owner = "Blank Label"


# Bug: Writing to the template blueprint instead of the stamped object
bob_cup = RetailOrderCup("Medium")
bob_cup.owner = "Bob"                   #used dot notation to write the name "Bob" onto the individual physical stamped object instead of corrupting the master class template
print(
    f"Blueprint Check -> Master: {RetailOrderCup} | Stamped Object Target: {bob_cup.owner}"
)


# Challenge 4
# Instruction: Use dot notation syntax layout parameters to read the size attribute into the variable
# customer_size, and then overwrite the contents attribute directly in-place with the string
# value "Espresso"
class BaristaStationCup:
    def __init__(self, size, owner):
        self.size = size
        self.owner = owner
        self.contents = "empty"


active_cup = BaristaStationCup("Small", "Chidi")
# Solve Here:
customer_size = active_cup.size  #used the dot notation to read the size attribute into the variable customer_size
# Update active_cup contents here:
active_cup.contents = "Espresso"  #set the contents attribute directly in-place with the string value "Espresso"
print(
    f"Active Transaction -> Size: {customer_size} | Contents Payload Matrix: {active_cup.contents}"
)


# Challenge 5
# Instruction: Based on your research on dunder formatting methods, implement an explicit
# __str__ hook inside the class that intercepts print commands and outputs a beautiful
# human-readable description string instead of a raw memory hex address
class InvoiceReceiptCup:
    def __init__(self, size, owner):
        self.size = size
        self.owner = owner

    # Implement your custom __str__ method hook here:
    # receipt_cup = InvoiceReceiptCup("Large", "Emeka")
    def __str__(self):                  #used the dunder method __str__ to implement an explicit hook inside the class that intercepts print commands and outputs a beautiful human-readable description string instead of a raw memory hex address
        return f"Receipt Invoice -> {self.size} cup reserved for: {self.owner}"


receipt_cup = InvoiceReceiptCup("Large", "Emeka")
print(receipt_cup)
