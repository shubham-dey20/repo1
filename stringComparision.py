from hashlib import shake_128
from itertools import count


'''s1="abcd"
s2="abcde"
if s1>s2:
    print(s1)
else:
    print(s2)'''

#print('new''line')

'''s1="Boost is the secret of my energy"
print(s1.split())
print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())
print(s1.capitalize())
print(s1.upper())'''


'''a=int(input())
s1=str(input())
for i in s1:
    if i == s1[a]:
        continue
    print(i,end='')'''


'''s1=str(input())
s2=str(input())
x=s1[1:]
y=s2[1:]
print(x+y)'''


'''s1=str(input())
s2=str(input())
print((s1*3)+s2)'''


'''s1=str(input())
s2=str(input())
print(s1.count(s2))'''


'''s1="hello"
print(s1[0]*2+s1[1]*2+s1[2]*2+s1[3]*2+s1[4]*2)'''

'''s1=str(input())
print("sa:",s1[0:len(s1):2])
print("sb:',s1[1:len(s1):2])'''


'''s1=str(input())
for i in s1:
    if i>="!" and i>="?":
        continue
print(i)'''

'''import string
s1=input("enter:")
s2=""
b=string.punctuation
for i in s1:
    if i not in b:
        s2=s2+i
print(s2)'''


'''s1=input("enter:")
s2=""
for i in s1:
    if i not in s2:
        s2=s2+i
for j in s2:
    print(j,"=",s1.count(j))'''

a=input()
b=len(a)//