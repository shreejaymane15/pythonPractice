import csv

name = input("What's Your name? ")
place = input("Where do you live? ")

with open("names.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, place])


    writer = csv.DictWriter(file, fieldnames=['name', 'place'])
    writer.writerow({"place":place, "name": name})