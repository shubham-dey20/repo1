'''n=1
while n<=10:
    print(n)
    n=n+1'''

'''s=0
n=1
while n<=10:
    s=s+n
    n=n+1
print("sum=",s)'''

from math import factorial
from tkinter import N


'''i=1
f=1
n=int(input("enter n:"))
while i<=n:
    f=f*i
    i=i+1
    print("factorial=",f)'''


'''i=1
while i<6:
    print(i)
    if(i==3):
        break
    i+=i'''

'''s=0
i=1
while i<=5:
    n=int(input("enter n:"))
    i=i+1
    if(n<0):
        continue
    s=s+n
print(s)'''

s=0
i=1
while i<=5:
    n=int(input("enter n:"))
    i=i+1
    if(n<0):
        break
    s=s+n
print(s)