r=int(input("enter the value of r"))
c=int(input("enter the value of c"))
s=[]
for i in range(r):
    n=[]
    print("enter the elements")
    for j in range(c):
        l=int(input())
        k=[l]
        n.extend(k)
    s.append(n)
for i in range(r):
    for j in range(c):
        print(s[i][j],end=" ")
    print()
