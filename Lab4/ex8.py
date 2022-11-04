import os

def ex8(path: str) -> list[str]:
    file_list = []
    for file in os.listdir(path):
        file_list.append(os.path.join(path, file))

    return file_list


print(ex8("C:\\Users\\Alin\\Desktop\\Anul3\\Python\\Lab1"))