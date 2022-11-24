import re

def get_xml_elements(path, attrs):
    # print("".join([f"{key} = \"{value}\" " for key, value in attrs.items()]))
    with open(path, "r") as f:
        text = f.readlines()
        for line in text:
            if re.search(r"[^<]\w\s*\w\s*\w\s=\s\"\w+\"", line) \
                    and any([re.search(f"{key} = \"{value}\"", line) for key, value in attrs.items()]):
                print(line)

get_xml_elements("ex4.xml", {"class": "url", "name": "url-form", "data-id": "item"})

