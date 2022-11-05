function1 = lambda *x,**y: sum([val for val in y.values()])

def function2(*x, **y):
    sum=0
    for i in y: sum = sum + int(y[i])
    return sum


print(function1(1, 4, b=10, c=6))