# Q39.Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}


marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print("Original Dictionary:")
print(marks)
print("Marks greater than 170:")
result = {key:value for (key, value) in marks.items() if value >= 170}
print(result)