def process(**kwargs):
    def Fibo(n):
        a = 0
        b = 1
        if n <= 0:
            print("Incorrect input")
            x = []
        elif n == 1:
            x = [b]
        else:
            x = [a, b]
            for i in range(2, n):
                c = a + b
                x += [c]
                a = b
                b = c
        return x    #one liner doesnt work "maximum depth reached"

    fibo = Fibo(1000)

    if "filters" in kwargs.keys():
        fibo = [f for f in fibo if all([p(f) for p in kwargs["filters"]])]
    if "offset" in kwargs.keys():
        fibo = fibo[kwargs["offset"]:]
    if "limit" in kwargs.keys():
        return fibo[:kwargs["limit"]]
    return fibo


def sum_digits(x):

    return sum(map(int, str(x)))

    
print(process(

    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2

))