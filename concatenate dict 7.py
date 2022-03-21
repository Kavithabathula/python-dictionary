# Q7.
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic={}
for i in dic1:
    if i in dic2:
        dic[i]=dic1[i]+dic2[i]
    elif i in dic2 and dic3:
        dic[i]=dic1[i]+dic2[i]+dic3[i]
    else:
        dic.update(dic1)
        dic.update(dic2)
        dic.update(dic3)
print(dic)


# from collections import Counter 
# dictionary1 = Counter({'kitkat': 10, 'MilkyBar': 5, 'diarymilk' : 50, 'munch' : 15}) 
# dictionary2 = Counter({'kitkat' : 7, 'diarymilk' : 5, })
# dictionary = dictionary1 + dictionary2 
# print("dictionary", str(dictionary))


# dictionary = {"orange" : 9, "Apple" : 5, "mango" : 25} 
# print("dictionary is : " + str(dictionary)) 
# result = (dictionary.values()) 
# print(result)