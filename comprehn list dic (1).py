

#list comp
data=[1,2,3,4,5,6,7,8,9]
l1=[i for i in data if(i%2!=0)]
print(l1)

x=20
print(["even" if x%2==0 else "odd"])


print([a*b for a in [1,2,3] for b in [4,5,6] ])

print([a for a in [1,22,33] for b in[1,33,44]if a==b])


'''

# dict comp
list=[1,2,3,4,5]
dict1={key:value for key,value in enumerate(list)}
print(dict1)
list=[1,2,3,4,5]
dict1={key:value for key,value in enumerate(list,6)}
print(dict1)

dict2={i:i+2 for i in range(10)}
print(dict2)

dict3={k:"python" for k in "codetantra"}
print(dict3)
'''







