def set_operations(a, b):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(set_operations(a, b))

#same as lab2?