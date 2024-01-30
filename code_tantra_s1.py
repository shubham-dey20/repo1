import re
mystring = "Hello!! Good Morning, Welcome topython tutorial class 24.For any  queries pleaseemail to contactus@codetantra.com"

print(re.findall('^Hello.+', mystring))
print(re.findall('[0-9]+', mystring))
print(re.findall('[a-z]+', mystring))
