def main():
    x = get_int("What's x? ")
    print(f"x is {x}")  


def get_int(prompt):
    while True:
        # Line where exception will occur
        try:
            x = int(input(prompt) )

        # Exception  handling block
        except ValueError:
            print("x is not an integer")
        
        # If you don't want to handle error but not doing anything
            #pass

        # Code to execute if no exception occurs
        else:            
            return x    

main()