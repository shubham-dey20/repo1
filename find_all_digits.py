import re
txt="That will be 59 dollars"
x=re.findall("\d",txt)
print(x)