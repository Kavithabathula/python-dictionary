def Merge(dict1,dict2):
    return(dict2.update(dict1))
dict1={"a":100,"b":200,"c":300}
dict2={"a":300,"b":200,"d":400}
print(Merge(dict1,dict2))
print(dict2)





# # Python code to merge dict using update() method
# def Merge(dict1, dict2):
#     return(dict2.update(dict1))
     
# # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
 
# # This return None
# print(Merge(dict1, dict2))
 
# # changes made in dict2
# print(dict2)