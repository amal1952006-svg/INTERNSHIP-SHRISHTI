students = [
    {"name": "arun", "marks": [80, 75, 90]},
    {"name": "meena", "marks": [23, 45, 33]}
]

students.append({"name": "ajay", "marks": [67, 80, 77]})

print(students)

for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])

    print(student["name"])

    if total > 250:
        print("Topper:", total)
    elif average > 60:
        print("Pass:", average)
    else:
        print("Fail:", average)

# while(True):
search=input("enter")
for i in students:
             #search=input("enter")
              if i["name"]==search:
                   print("found",i)
                   break
else:
                   
                  print("not found")
students.pop()
print(students)
students.sort(key=lambda x: sum(x["marks"]) / len(x["marks"]))
print(students)
if average >= 50:
        print(student["name"], average, "passed students")
print(len(students))

newname = input("Enter student name: ")

for s in students:
    if s["name"] == newname:
        print("already exited")
        break
else:
        print("not exited")