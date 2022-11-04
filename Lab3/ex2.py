'''
aici nu ar trebui sa aplici set musai, dar sure
'''
def count_letters(s):
    return {i: s.count(i) for i in set(s)}

print(count_letters("Helllloooooo"))

#mai simplu asa

