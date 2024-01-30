import re
str1 = "Hello how are this is ython"
b = re.search("^Hello..", str1)
print(b.span())
print(b.group())
