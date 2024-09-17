students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",}    # {key, value}


# print all dictionary
print("Dictionary: \n")
print(students)

# print specific
print("\nSpecific key value:\n")
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# For loop
print("\nOnly Keys\n")
for student in students:
    print(student)  # Only prints keys


# For loop
print("\nBoth Keys and Values\n")
for student in students:
    print(student, students[student], sep=", ")
