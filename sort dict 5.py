# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}



# dictI={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# d={}
# for i in sorted (dictI):
#     print(i,end=" ")
#     d.update(dictI)
# print(d)


# import operator
# # d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print('Original dictionary : ',d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(1))
# print('Dictionary in ascending : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending: ',sorted_d)