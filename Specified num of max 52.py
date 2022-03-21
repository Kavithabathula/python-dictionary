# Q52. Write a Python program to find the specified number of maximum values in a given
# dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:

# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']

def test(dictt, N):
    result = sorted(dictt, key=dictt.get, reverse=True)[:N]
    return result 
dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
print("\nOriginal Dictionary:")
print(dictt)
N = 1
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dictt, N))
N = 2
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dictt, N))
N = 5
print("\n",N,"maximum value(s) in the said dictionary:")
print(test(dictt, N))