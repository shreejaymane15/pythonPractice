students= ["Hermione", "Ron", "Harry"]

# print all list
print(students)

# print specific 
print("\nSpecific Student\n")
print(students[0])   # Hermione
print(students[1])  # Ron
print(students[2])  # Harry
print(students[-1])  # Harry

# print all with loop
print("\nFor Loop Student\n")
for i in students:
    print(i)

# print all with alternate method
print("\nFor Loop Student\n")
for i in range(len(students)):
    print(i)

