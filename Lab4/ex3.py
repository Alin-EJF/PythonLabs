import os 

def tail_20(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()[-20:]


def count_extension(path: str) -> list[tuple[str, int]]:
    extension_set = {}
    for file in os.listdir(path):
        extension = os.path.splitext(file)[1][1:]
        if extension in extension_set:
            extension_set[extension] += 1
        else:
            extension_set[extension] = 1

    return sorted(extension_set.items(), key=lambda x: x[1], reverse=True)


def ex3(my_path: str):
    if os.path.isfile(my_path):
        return tail_20(my_path)

    return count_extension(my_path)


print(ex3("C:\\Users\\Alin\\Desktop\\files_with_A.txt"))
print(ex3("C:\\Users\\Alin\\Desktop"))