students = [
    {"name": "Hermione", "houses":"Gryffindor"}, 
    {"name": "Harry", "houses":"Gryffindor"}, 
    {"name": "Ron", "houses":"Gryffindor"}, 
    {"name": "Padma", "houses":"Ravenclaw"}, 
    {"name": "Draco", "houses":"Slytherin"}
]


# No duplicates allowed
houses = set()

for student in students:
    houses.add(student["houses"])


for house in sorted(houses):
    print(house)
