

'''def checker():
    i=0
    u=l=d=s=sw=0
    for i in n:
        if(i>='a' and i<='z'):
            l=l+1
        elif(i>='A' and i<='Z'):
            u=u+1
        elif(i>='0' and i<='9'):
            d=d+1
        elif(i==" "):
            sw=sw+1
        else:
            s=s+1
    return l,u,d,s,sw
n=input("n: ")
l1,u1,d1,s1,sw1=checker()
print("Upper case:",u1)
print("Lower case:",l1)
print("Digit:",d1)
print("White Spaces:",sw1)
print("symbol:",s1)'''

'''def email_slicer(email):
    username, _, domain = email.strip().partition("@")
    return f"Your username is {username} & domain is {domain}"
user_input = input("Enter Your Email: ")
print(email_slicer(user_input))'''

n=int(input("n:"))
for i in range(n):
    email = input("Enter Your Email: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print("Your username is",username ,"& domain is", domain.upper())