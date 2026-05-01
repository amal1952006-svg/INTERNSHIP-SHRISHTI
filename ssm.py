student={"name":"arun","mark":[80,75,90]},
        {"name":"meena","mark":[23,45,33]}
student.append{"name":"ajay","mark":[67,77,90]}
print(student)
for students in student:
        total=sum(students["marks"])
        average=total/len(student["marks"])
        print["name"]
        if total>250:
                print("topper",total)
        elif average>60:
                print("pass",average)
        else:
                print("fail",average)