import re

def replace(x):
    print([re.sub(f"^.{{i}}[et]", x.group()[0:i] + '*', x.group()) for i in range(len(x.group())) if i%2==0])

    return re.sub(r'^.{2}[et]', r'*', x.group())


def censor(text):
    return re.sub(r'[aeiouAEIOU]\w*[aeiouAEIOU]', replace, text)


print(censor("Acela este un ou alb"))
