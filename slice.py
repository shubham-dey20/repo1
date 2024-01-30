'''s1="How are you?"
print(s1[4]+s1[5]+s1[6])
print(s1[8]+s1[9]+s1[10])
print(s1[8]+s1[9]+s1[10]+s1[11])
print(s1[-2]+s1[-3]+s1[-4])'''


'''s2="sking"
print(s2[0]+s2[3:])
print(s2[1]+s2[2]+s2[3])'''




s3="AabAcda"
p=""
for char in s3:
    if char not in p:
        p=p+char
print(p)