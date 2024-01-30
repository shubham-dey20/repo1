'''l1=list(input("l1:").split(','))
l2=list(input("l2:").split(','))
d1=dict(zip(l1,l2))
print(d1)
d2=dict(zip(l2,l1))
print(d1.update(d2))'''

'''troupe = {('Cleese', 'John') : [1, 2, 3],
			('Chapman', 'Graham') : [4, 5, 6],
			('Idle', 'Eric') : [7, 8, 9],
			('Jones', 'Terry') : [10, 11, 12],
			('Gilliam', 'Terry') : [13, 14, 15, 16, 17, 18],
			('Palin', 'Michael') : [19, 20]}

for last, first in sorted(troupe):      
	print (first, last, troupe[last, first])'''

'''a=input("data1: ").split(",")
b=input("data2: ").split(",")
mydict=dict(zip(a,b))
print(sorted(mydict.items()))'''


#enter 2 user defined list create a new list 
l1=list(map(int,input("l1:").split(',')))
l2=[]
r=0
s1=0
s2=0
for i in l1:
	if i>0 and i<100:
		l2.append(i)
print(l2)
for i in l2:
	l=i%10
    r=(r*10)+l
    s1=s1+l
    s2=s2+l**3
    i=i//10
print(r)
if (n==r):
    print("palindrome")
else:
    print("not p")