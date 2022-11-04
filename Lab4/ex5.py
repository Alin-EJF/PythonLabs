import os

def search_recursive(target: str, to_search: str) -> list[str]:
    file_list = []
    if os.path.isfile(target):
        with open(target, 'rb') as file:
            if to_search in file.read():
                file_list.append(target)
    else:
        for file in os.listdir(target):
            file_list += search_recursive(os.path.join(target,
                                          file), to_search)

    return file_list


def ex5(target: str, to_search: str):
    if not os.path.exists(target):
        raise ValueError(f"Error, target must be directory or file \"{target}\"?")

    return search_recursive(target, bytes(to_search, 'utf-8'))

#print(ex5("C:\\Users\\Alin\\Desktop\\Anul3\\Python\\Lab1", "def"))
#print(ex5("C:\\Users\\Alin\\Desktop\\Anul3\\Python\\Lab1\\ex1.py", "def"))