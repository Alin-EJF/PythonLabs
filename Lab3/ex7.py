def extract_number(text):
    number = ''
    for char in text:
        if char.isdigit():
            number += char
        elif number != '':
            break
    return int(number)

print(extract_number("An 12 apple is 123 USD 1232"))