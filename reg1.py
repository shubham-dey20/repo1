import re
str1 = "Hellop this is ython"
x = re.search("^He.*on$", str1)
print(x)