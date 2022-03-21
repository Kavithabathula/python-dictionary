# Q3.Write a Python script to generate and print a dictionary that contains a number (between 1
# and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

dict={1,2,3,4,5,6,7,8,9,}

a={}
for i in range(1,10):
    b={i:i*i}
    a.update(b)
print(a)