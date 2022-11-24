import re
import os

def good_files(directory, regex):
    result = []
    for root, dirs, files in os.walk(directory):
        for f in files:

            ok = 0
            if re.search(regex, f):
                file_name = os.path.join(root, f)
                try:
                    with open(file_name, "r") as f_d:
                        for line in f_d:
                            if re.search(regex, line):
                                ok = 1
                                break
                except Exception as e:
                    print(e)
                    continue

                if ok == 0:
                    result += [f]
                else:
                    result += [">>" + f]

    return result


print(good_files("C:\\Users\\tdgal\\OneDrive\\Desktop", r'_Tema[1-3]_ML_[1-9]{3}'))
