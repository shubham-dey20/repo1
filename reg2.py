import re
str1 = "Hello this is python"
b = re.search("\s", str1)
print(b.start())
b = re.search("\s", str1)
print(b.end())
