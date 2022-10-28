def loop(mapping):
    to_return = list()
    value = mapping['start']
    while value not in to_return:
        to_return.append(value)
        value = mapping[value]
    return to_return

    
print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))