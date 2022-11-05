def even_odd(integers):
    return list(zip([i for i in integers if i % 2 == 0], [i for i in integers if i % 2 != 0]))

print(even_odd([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))