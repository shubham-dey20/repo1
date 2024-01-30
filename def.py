'''a=100
def d():
    print(a)
    a=20
    print(a)
d()
print(a)'''


'''a=100
def d():
    global a
    print(a)
    a=20
d()
print(a)'''


def fact(x):
    if(x==0 | x==1):
        return 1
    else:
        return x*fact(x-1)
x=int(input("n:"))
f=fact(x)
print(f)