'''r=0
s1=0
s2=0
n=int(input("enter no:"))
while (n>0):
    l=n%10
    r=(r*10)+l
    s1=s1+l
    s2=s2+l**3
    n=n//10
print(r)
if (n==r):
    print("palindrome")
else:
    print("not p")'''



'''n=int(input("enter a no."))
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
        break
if(c==0):
    print("prime")
else:
    print("not prime")'''


'''a= int(input("Enter no : "))
b= int(input("Enter no: "))
s=0
for n in range(a,b+1):
    if n>0:
        s=s+n
print(s)'''

'''s=0
i=1
while i<21:
    n=int(input("enter no."))
    if n>0:
        s=s+n
        i=i+1
print("sum=",s)'''


'''s="Aabc@123"
upper=lower=digit=0
for i in s:
    if i>="a" and i<="z":
        upper=upper+1
    elif i>="A" and i<="Z":
        lower+=1
    
    elif i>="0" and i<="9":
        digit+=1
    else:
        print(i)
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)'''


'''a=int(input("enter 1st no."))
b=int(input("enter 2nd no."))
if a>b:
    smaller=b
else:
    smaller=a
for i in range(1, smaller+1):
    if a%i==0 and b%i==0:
        hcf=i
print("hcf=",hcf)'''

'''n=int(input("n:"))
for i in range(1,n+1):
    for k in range (1,i+1):
        print("*",end="")
    print()'''

'''n=int(input("n:"))
for i in range(1,n+1):
    for k in range (1,i+1):
        print(" * ",end="")
    print()'''


'''s1=0
s2=0
n=int(input("enter no:"))
while (n>0):
    l=n%10
    s1=s1+l
    s2=s2+l**3
    n=n//10
if (s2==n):
    print("armstrong no.")
else:
    print("not a")'''