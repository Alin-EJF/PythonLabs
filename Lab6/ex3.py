import re

def match_strings(strings, regexes):
    result = []
    for string in strings:
        for regex in regexes:
            if re.search(regex, string):
                result += [string]
                break
    return result


print(match_strings(["abc_", "def", "AB","92"], ["[A-Z]", "[0-9]+"]))

