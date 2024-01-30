#divisible by 7
'''a=int(input("enter a number:"))
if a%7==0:
    print("given number",a,"is divisible by 7")
print("end of program")'''

#even or odd
'''a=int(input("a="))
if a%2==0:
    print(a,"is even")
else:
     print(a,"is odd")
print("next prg")'''

#sum of two +ve numbers
'''a=int(input("a:"))
b=int(input("b:"))
if a>0 and b>0:
    print("sum=",a+b)
else:
    print("syntax error")'''

#electricity bill
'''a=int(input("units="))
if a>=1 and a<=100:
    print("electricity bill=",a*1.5)
elif a>=101 and a<=200:
    print("electricity bill=",a*2.5)
elif a>=201 and a<=300:
    print("electricity bill=",a*4)
elif a>=301 and a<=350:
    print("electricity bill=",a*5)
else:
    print("electricity bill=",a*15)'''

#BMI
'''w=float(input("Enter your weight(in pounds): "))
h=float(input("Enter your height(in inches): "))
bmi=(w*0.45359237)/((h*0.0254)**2)
print("Your BMI is",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obese")'''

#better package
'''p1=eval(input("Enter the weight and cost of Package1:"))
p2=eval(input("Enter the weight and cost of Package2:"))
if p1<p2:
    print("p1 is better")
elif p2<p1:
    print("p2 is better")
else:
    print("buy any one you want")'''

#type of triangle
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))
if a==b== c:
	print("equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")
else:
	print("scalene triangle")