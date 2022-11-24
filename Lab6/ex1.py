import re

def extract_words(text):
    return re.findall("[a-zA-Z0-9]+", text)
    # re.findall(r'\w+', text)


print(extract_words("Some text with 2 n4mbers and 1000 words"))

