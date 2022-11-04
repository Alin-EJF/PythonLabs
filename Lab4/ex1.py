import os


def get_unique_extension(path: str):
    extension_set = set()
    for file in os.listdir(path):
        extension = os.path.splitext(file)[1][1:]
        if extension != '':
            extension_set.add(extension)

    extension = list(extension_set)
    return sorted(extension)

print(get_unique_extension('C:\\Users\\Alin\\Desktop'))