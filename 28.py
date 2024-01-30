'''n = int(input())
sum = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
           break
    else:
        sum = sum + i
print(sum)'''

'''r=0
n=int(input("enter no:"))
while n>0:
    l=n%10
    r=(r*10)+l
    n=n//10
    if r==n:
        print(r)'''

a= int(input("Enter no : "))
b= int(input("Enter no: "))

for n in range(a,b+1):
    t=n
    r= 0

    while(t > 0):
        l= t % 10
        r = (r * 10) + l
        t = t //10

    if(n == r):
        print("%d " %n, end = '  ')