'''
aici era ideea sa ai mai multe numere de la tastatura si sa faci cmmdc-ul tuturor, also, vezi ca nu validezi input-ul, pot baga acolo niste litere si crapa
'''

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
