# if 
print("Test if\n")
x = int(input("What's x? "))

y = int(input("What's y? "))


if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal than y")


# else if
print("\nTest else if\n")

x = int(input("What's x? "))

y = int(input("What's y? "))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal than y")


# else
print("\nTest else\n")

x = int(input("What's x? "))

y = int(input("What's y? "))


if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal than y")


# or
print("\nTest or\n")

x = int(input("What's x? "))

y = int(input("What's y? "))


if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal than y")
