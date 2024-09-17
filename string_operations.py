name = input("Enter your name: ")

# Remove whitespace from string from left and right
name = name.strip()

# For only left side
name.lstrip()

# For only right side
name.rstrip()

# Capitalize only one word 
name = name.capitalize()

print(name)

# Capitalize user's name 
name = name.title()

print(name)

# Another Approach
name = name.strip().title()

print(name)

# Split user's name into first name and last name

fullName = input("Enter Full Name: ")

first, last = fullName.split(" ")

print(first)
print(last)



