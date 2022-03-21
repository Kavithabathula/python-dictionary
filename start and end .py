a=["a","b","c","d"]
b=["e","f","g","h"]
i=0
d={}
while i<len(a):
    c=a[i]+b[-i]
    d.update({i:c})
    i+=1
print(d)