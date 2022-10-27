def unique_in_list(lista):
    return len(set(lista)), len(lista) - len(set(lista)) 

print(unique_in_list([1, 2, 3, 4, 5, 1, 2, 3]))
