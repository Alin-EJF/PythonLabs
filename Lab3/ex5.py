def validate_dict(rules, dictionary):
    rules_dict = {rule[0]: [rule[1], rule[2], rule[3]] for rule in rules}
    return all([key in rules and value.startswith(rules_dict[key][1]) and
                rules_dict[key][2] in value and value.endswith(rules_dict[key][3])
                for key, value in dictionary.items()])

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} , {"key1": "come inside, it's too cold out", "key3": "this is not valid"} ))