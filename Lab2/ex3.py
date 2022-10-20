def setOperations(a, b):
    return (list(set(a) & set(b)), list(set(a) | set(b)), list(set(a) - set(b)), list(set(b) - set(a)))

list_a = [1, 2, 3]
list_b = [3, 4, 5]

print(setOperations(list_a, list_b))