# dict =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']
#         }
# count=0
# for i in dict:
#     count+=1
# print(dict)
# print(count)



dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
k=list(dict.values() )
c=0
for i in k:
   for j in i:
   	c+=1
print(c)