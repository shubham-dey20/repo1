import re
str1 = "Hellop this is ython"
z = re.split("\s", str1)
print(z)

a = re.sub("\s", "", str1)
print(a)
