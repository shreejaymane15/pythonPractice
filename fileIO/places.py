with open("names.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        print(f"{name} is in {place}")
    