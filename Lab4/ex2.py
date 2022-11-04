import os 

def write_files_with_A(path: str, write_file: str):
    with open(write_file, 'w') as f:
        for file in os.listdir(path):
            if file[0] == 'A' or file[0] == 'a':
                f.write(os.path.join(path, file) + '\n')


write_files_with_A("C:\\Users\\Alin\\Desktop","C:\\Users\\Alin\\Desktop\\files_with_A.txt")
