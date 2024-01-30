#program make a calculator
#add two function
def add(x,y):
    return x+y
#sub two function
def subtract(x,y):
    return x-y

#multiply two function
def multiply(x,y):
    return x*y

#divide two function
def divide(x,y):
    return x/y

print("selection oprator")
print("a.add")
print("b.subtract")
print("c.multyply")
print("d.divide")

choice=input("enter your choice a/b/c/d")

num_1=int(input("enter your first number"))
num_2=int(input("enter your second number"))

if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))
else:
    print("this is an invalid")


