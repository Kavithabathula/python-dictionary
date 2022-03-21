my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
    s=i
print(max) 
max1=0
for i in my_dict:
    if my_dict[i]>max1:
        if max!=my_dict[i]:
            max1=my_dict[i]
print(max1) 
max2=0
for i in my_dict:
    if my_dict[i]>max2:
        if max!=my_dict[i] and max1!=my_dict[i]:
            max2=my_dict[i]
print(max2)

# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.
d= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
a=[ ]
for i in d:
    if d[i]>50:
        s=i
        a.append(i)
print(a)