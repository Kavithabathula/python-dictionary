# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

j=input("enter")
c={"ball":"red","bat":4,"wickets":8}
dic=c.keys()
if j in dic:
    print("yes,key is exist")
else:
    print("no,key is not exixt")