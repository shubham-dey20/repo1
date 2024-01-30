n=int(input("n:"))
for i in range(n):
    email = input("Enter Your Email: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print("Your username is",username ,"& domain is", domain.upper())
