
names = []

with open("names.txt", "r") as file:

#     lines = file.readlines()
# for line in lines:
#     print("hello,", line.rstrip())



    # for line in file:
    #     print("hello,", line.rstrip())





#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")




    for line in sorted(file, reverse=True):
        print(f"hello, {line.rstrip()}")
