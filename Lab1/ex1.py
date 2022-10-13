import sys

def cmmdc(a, b):
    while b:
        a, b = b, a % b
    return a



def cmmdc2(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

def main():
   
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(cmmdc(a, b))

main()