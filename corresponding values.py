a=["one","two","three","four","five"]
b=[1,2,3,4,5]
dict={}
for i in range(len(a)):
    dict.update({a[i]:b[i]})
print(dict)