import re

def substrings(regex, text, x):
    return [word for word in re.findall(regex, text) if len(word) == x]


print(substrings('\w+', "Some text with 2 numbers and 100 words", 3))

