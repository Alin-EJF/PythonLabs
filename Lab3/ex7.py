def operations(*sets):

    result = {}
    for idx1 in range(0, len(sets) - 1):
        for idx2 in range(idx1 + 1, len(sets)):
            result.update({(str(sets[idx1]) + " | " + str(sets[idx2])): (sets[idx1] | sets[idx2]),
                           (str(sets[idx1]) + " & " + str(sets[idx2])): (sets[idx1] & sets[idx2]),
                           (str(sets[idx1]) + " - " + str(sets[idx2])): (sets[idx1] - sets[idx2]),
                           (str(sets[idx2]) + " - " + str(sets[idx1])): (sets[idx2] - sets[idx1])})
    return result


print(operations({1, 2}, {2, 3}))