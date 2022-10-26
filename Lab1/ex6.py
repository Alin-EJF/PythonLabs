"""
def palindrom(n):
    m = 0

    while n:
        m = m * 10 + n % 10
        n //= 10

        if m == n or m == n // 10:
            return True

    return False
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    n = int(input())

    print(is_palindrome(n))

main()
