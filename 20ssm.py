students = [
    {"name": "arun", "marks": [80, 75, 90]},
    {"name": "meena", "marks": [23, 45, 33]},
    {"name":"raj","marks":[88,80,95]}
]

students.append({"name": "ajay", "marks": [67, 80, 77]})

print(students)

for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])

    print(student["name"])
    print("total",total)
    print("average",average)

    if average>=85:
        print("Topper", student["name"])
    elif average > 60:
        print("Pass")
    else:
        print("Fail")

search=input("enter: ")
for i in students:
             
              if i["name"]==search:
                   print("found",i)
                   break
              else:
                   
                  print("not found")
remove=input("enter student to be removed: ")
for i in students:
    
    if i["name"]==remove :
         students.remove(i)
         print("after removing",students)
         break
         

students.sort(key=lambda x: sum(x["marks"]) / len(x["marks"]))
print("after sorting:",students)

for n in students:
        avg = sum(n["marks"]) / len(n["marks"])
        if avg>=50:
            print(n["name"], avg, "passed students")
print("count:",len(students))

newname = input("Enter student name: ")

for s in students:
    if s["name"] == newname:
        print("already exited")
        break
else:
        print("not exited")