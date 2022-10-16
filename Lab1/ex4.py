'''
aici nu prea tratezi bine corner case-uri, daca iti dau un 'A' la tine imi returneaza '_a' si ar trebui doar 'a', ar trebui sa incerci totusi sa te folosesti
de faptul ca sunt UpperCamelCase strings, adica incep cu litera mare din start, dupa ideea pe care ai folosit-o e buna
'''

def camel_to_snake(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_"
        snake += c.lower()
    return snake

def main():
    s = input()
    print(camel_to_snake(s))
