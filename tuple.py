'''x=str(input("x:"))
y=str(input("y:"))
z=x+y
print("x=",x,"y=",y,"z=",z, sep=",")'''

'''u=int(input("u:"))
v=int(input("v:"))
a=complex(u,v)
b=format(u,"b")
print(a,b, sep="@")'''


n=int(input())
l=[]
for i in range(n):
    s=input().split(",")
    c=0
    for j in s:
        if j.isalpha()==True:
            c+=1
    if c==len(s):
        l.append(tuple(s))
print(l)