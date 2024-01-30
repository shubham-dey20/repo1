'''a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
if a>b:
    largest=a
else:
    largest=b
for i in range(1, largest+1):
    if a%i==0 and b%i==0:
        LCM=i*i
        i=i+1
print("LCM",LCM)'''


'''i=1
f=1
n=int(input("enter n:"))
while(i<=n):
    f=f*i
    i=i+1
print("factorial",f)'''

'''#ASCII
a=str(input())
for i in a:
    print(ord(i))'''


'''t1=('hello','python','good')
t1=input("t1:")
y=list(t1)
y.append('morning')
t1=tuple(y)
print(t1)'''


'''a=input("a:").split(",")
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''


a=list(map(int,input("a:").split(',')))
