d=[]
#task=input("enter")
def add_task():
    task=input("enter")
    for i in range(5):
        #print("name",task)
        d.append(task)
    print(d)
add_task()
r={}
time=int(input("enter"))
pri=input("enter")
def analyze():
    print(time)
    print(pri)
analyze(4,"low")
