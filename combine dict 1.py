# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


from typing import Counter

dict1={"a":100,"b":200,"c":300}
dict2={"a":300,"b":200,"d":400}
d=Counter(dict1)+Counter(dict2)
print(d)



s={"sonu":21,"Ram":36,"Amar":69}
a={"python":69,"java":98,"dev":67}
c={}
for i in (s,a):
    c.update(i)
print(c)