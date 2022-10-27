def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key not in dict2:
            return False
        if type(dict1[key]) == dict:
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        elif type(dict1[key]) == list:
            if dict1[key] != dict2[key]:
                return False
        elif type(dict1[key]) == set:
            if dict1[key] != dict2[key]:
                return False
        else:
            if dict1[key] != dict2[key]:
                return False
    return True

print(compare_dicts({1: {6: 9, 8: 0}, 3: (1, 4, 6)}, {1: {6: 9, 8: 0}, 3: (1, 4, 6)}))
print(compare_dicts({1: {6: 9, 8: 5}, 3: (1, 4, 6)}, {1: {6: 9, 8: 0}, 3: [1, 4, 6, 7]}))