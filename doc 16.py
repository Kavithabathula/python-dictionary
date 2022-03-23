# Q16.Write a Python program to map two lists into a dictionary.

l=["red","orange","black"]
k=[1,2,3]
d={}
for i in l:
    for j in k:
        d[i]=j
        k.remove(j)
        break
print(d)