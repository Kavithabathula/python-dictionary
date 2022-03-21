# l="MISSIIPPI"
# j=list(l)
# f={}
# for item in j:
# 	if item in f:
# 		f[item]+=1
# 	else:
# 		f[item]=1
# print(f)


c="MISSISSIPPI"
l={}
i=0
while i<len(c):
	j=0
	count=0
	while j<len(c):
		if c[i]==c[j]:
			count+=1
		j+=1
	l[c[i]]=count
	i+=1
print(l)