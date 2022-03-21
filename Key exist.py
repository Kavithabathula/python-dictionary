# dict={"name":"Raju","marks":93}
# a=input("enter")
# if a in dict:
#     print("Exist")
# else:
#     print("Not exist")
    
dict={'name':'raju','marks':5}
user=input("enter")
if user in dict:
    print('correct')
if user=='name':
    print('exist')
elif user=='class':
    print('not exist')
else:
    print('never exist')