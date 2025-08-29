marks = {
    "alice" : 85,
    "tony" : 78
}

x = input("enter student name :")

if x in marks:
    print("{}'s marks is :{}".format(x,marks[x]))
else:
    print("student not found")