dict={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    }
    
a={}
for i in dict:
    if dict[i] not in a:
        s=i
print(dict)


# o/p={"ball":"red","bat":4,"wickets":8