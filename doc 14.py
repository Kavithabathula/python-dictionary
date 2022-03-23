# Q14.Write a Python program to multiply all the items in a dictionary.

dic={"a":2,"b":2,"c":3}
multi=1
for i in dic:
    multi=multi*dic[i]
print(multi)