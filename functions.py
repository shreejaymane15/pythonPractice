# Function Defination
def hello1():
    print("Hello,")


name = input("What's your name? ")
# Function Call
hello1()
print(name)





# Function Defination with parameter
def hello2(to):
    print("Hello,", to)


name = input("What's your name? ")
# Function Call
hello2(name)




# Function Defination with parameter with default value
def hello3(to = "world"):
    print("Hello,", to)


hello3()
name = input("What's your name? ")
# Function Call
hello3(name)