def numbers_found(list):
    return [i for i in list if type(i) in  [int, float, complex]]

print(numbers_found([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))