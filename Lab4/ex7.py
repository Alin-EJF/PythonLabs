import os


def specs(file_path: str) -> dict:
    return {
        "full_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[1][1:],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK)
    }


print(specs("C:\\Users\\Alin\\Desktop\\files_with_A.txt"))