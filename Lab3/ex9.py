def my_function(*arguments, **keywords):
    return len([el for el in arguments if el in keywords.values()])


print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))