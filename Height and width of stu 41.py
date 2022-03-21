# Q41.Write a Python program to filter the height and width of students, which are stored in a
# dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
# 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

def filter_data(students):
    result = {k: s for k, s in students.items() if s[0] >=6.0 and s[1] >=70}
    return result    
 
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary:")
print(students)
print("\nHeight > 6ft and Weight> 70kg:")
print(filter_data(students))