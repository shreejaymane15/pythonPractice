import csv

students = []

with open("names.csv") as file:
    
    # for line in file:
    #     name, place = line.rstrip().split(",")
    #     student = {"name": name, "place": place}
    #     students.append(student)
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "place": row["place"]})





# def get_name(student):
#     return student["name"]


# for student in sorted(students, key=get_name):
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['place']}")