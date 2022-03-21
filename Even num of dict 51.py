# Q51.Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}



def test(dictt):
    result = {key: [idx for idx in val if not idx % 2]  
          for key, val in dictt.items()}   
    return result    

students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
print("\nOriginal Dictionary:")
print(students)
print("Filter even numbers from said dictionary values:")
print(test(students))

students = {'V' : [1, 3, 5], 'VI' : [1, 5], 'VII' : [2, 7, 9]} 
print("\nOriginal Dictionary:")
print(students)
print("Filter even numbers from said dictionary values:")
print(test(students))