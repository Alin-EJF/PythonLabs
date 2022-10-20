def is_palindrome(n):
    return str(n) == str(n)[::-1] #ty for the tip

def greatest_palindrome(nrs):
    greatest_palindrome = []
    for nr in nrs:
        if is_palindrome(nr):
            greatest_palindrome.append(nr)
    return (len(greatest_palindrome), max(greatest_palindrome))

print(greatest_palindrome([1, 2, 15, 100, 171, 191]))