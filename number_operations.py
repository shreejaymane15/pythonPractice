a = input("What's X : ")
b = input("What's Y : ")

z = int(a) + int(b)

print(z)


# Another Approach

x = int(input("What's X : "))
y = int(input("What's Y : "))


print(x + y)


# Float Input

x = float(input("What's flaot X : "))
y = float(input("What's float Y : "))


print(x + y)


# Round Function
print("\nTest Round Function\n")

x = float(input("What's flaot X : "))
y = float(input("What's float Y : "))

z = round(x + y)

print(z)

# Add comma to result automatically
print("\nTest Comma Output\n")

x = float(input("What's flaot X : "))
y = float(input("What's float Y : "))

z = round(x + y)

print(f"{z:,}")

# Round Function for specific decimal
print("\nTest Round Function For Specific Decimal\n")

x = float(input("What's flaot X : "))
y = float(input("What's float Y : "))

z = round(x / y, 2)

print(z)


# Format String Function for specific decimal
print("\nTest Round Function For Specific Decimal\n")

x = float(input("What's flaot X : "))
y = float(input("What's float Y : "))

z = x / y

print(f"{z:.2f}")


