myDict=[
 {"first":"1"}, 
 {"second": "2"}, 
 {"third": "1"}, 
 {"four": "5"}, 
 {"five":"5"}, 
 {"six":"9"},
 {"seven":"7"}
]

j=[]
for i in range(len(myDict)):
        for l in myDict[i]:
                if myDict[i][l] not in j:
                        j.append(myDict[i][l])
print(j)