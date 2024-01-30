'''f=1
n=int(input())
for i in range(1,n+1):
    f=f*i
    i=i+1
print(f)'''


'''a=0
b=1
n=int(input("n:"))
for i in range(2,n+1):
    s=a+b
    print(s,end="")
    a=b
    b=s'''

'''def Fibonacci(n):

    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

n=int(input("n:"))
print(Fibonacci(n))'''

'''def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = str(input("s:"))
print("reverse:", end="")
print(reverse(s))'''

'''r=0
def reverseno(n):
    global r
    l=n%10
    r=(r*10)+l
    n=n//10
    if n==0:
        return r
    else:
        return("not r")

n=int(input("n:"))
print(reverseno(n))'''



'''d=input("d: ")
l1=d.split(",")
for i in range(0,len(l1)):
    l1[i]=int(l1[i])
    if (l1[0]==3) or (l1[-1]==3):
        print("True")
    else:
        print("False")'''




'''def Fibonacci(n):

    if n < 0:
        print("Incorrect input")
 
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

n=int(input("n:"))
print(Fibonacci(n))
for i in range(1,n+1):
    print(Fibonacci(i))'''


'''r=0
def reverseno(n):
    for i in range(1,n+1):
        global r
        l=n%10
        r=(r*10)+l
        n=n//10
        if n==0:
            return r
        else:
            return ("not r")
n=int(input("n:"))
print(reverseno(n))'''

r=0
n=int(input("n:"))
for i in range(1,n+1):
    l=n%10
    r=(r*10)+l
    n=n//10
    print()