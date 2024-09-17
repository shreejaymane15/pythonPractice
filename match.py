name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor") 
    
    case "Draco":
        print("Slythrin")
    
    case _:
        print("Who?")