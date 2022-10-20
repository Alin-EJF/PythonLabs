def ascii_divisible_by_x(x=1, strings=[], flag=True):
    result = []
    for string in strings:
        result.append([char for char in string if (ord(char) % x == 0) == flag])  #stolen, cute
    return result

print(ascii_divisible_by_x(2, ["test", "hello", "lab002"], False))