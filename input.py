# Ask User For Their Name
name = input("What's your name? ")

"""
This program asks the user for their name and then 
responds with a personalized greeting. 
"""

# String Concatenation
print("hello, "+ name)

# print function parameters
print("hello, ", end="")
print(name)

# print function parameters
print("hello,", name, sep=" ")

# Format String
print(f"hello, {name}")

