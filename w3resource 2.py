# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}


# l="W3RESOURCE"
# j=list(l)
# f={}
# for item in j:
# 	if item in f:
# 		f[item]+=1
# 	else:
# 		f[item]=1
# print(f)


# c="W3RESOURCE"
# l={}
# i=0
# while i<len(c):
# 	j=0
# 	count=0
# 	while j<len(c):
# 		if c[i]==c[j]:
# 			count+=1
# 		j+=1
# 	l[c[i]]=count
# 	i+=1
# print(l)