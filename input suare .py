num=int(input("enter"))
d={}
for i in range(num):
    x={i:i*i}
    d.update(x)
print(d)