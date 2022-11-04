import os
import ex1


def ex4() -> list[str]:
    path = input("Path: ")
    return ex1.get_unique_extension(path)


print(ex4())