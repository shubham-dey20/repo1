import re
txt="Hello@World"
x=re.findall("^Hello World$",txt)
if x:
    print("Yes, the string matches the regular expression")
else:
    print("No match")