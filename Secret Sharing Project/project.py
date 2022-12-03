import sys
import re
from mod import Mod
from os import urandom

global P  #large prime number (harder to crack)
P = 2**521 - 1

"""
def int_from_bytes(s):
    acc = 0
    for b in s:
        acc = acc * 16
        acc += b
    return acc
"""

def int_from_bytes2(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def evaluate(coefficients, x):
    acc = 0
    power = 1
    for c in coefficients:
        acc += c * power
        power *= x
    return acc


def retrieve_original(secrets ,P):
    x_s = [s[0] for s in secrets]
    acc = Mod(0, P)
    for i in range(len(secrets)):
        others = list(x_s)
        cur = others.pop(i)
        factor = Mod(1, P)
        for el in others:
            factor *= el * (el - cur).inverse
        acc += factor * secrets[i][1]
    return acc


def check_equality(retrieved_secret, secret): 
    if retrieved_secret == secret:
        print("retrieved_secret == secret TRUE")
    else:
        print("retrieved_secret == secret FALSE")


def split(n,m,file):
    print("\n Splitting \n")

    if m > n:
        print("error: m can't be bigger than n")
        return

    try:
        secret = open(file,"r").read()
    except:
        print("error: file not found or can't be opened")
        return

    secret = int_from_bytes2(secret.encode("utf-8"))    
    #print(secret)
    #print(int_to_bytes(secret))

    
    if(secret < P):
        print("YES, secret < P checked")
    
    
    secret = Mod(secret, P)

    polynomial = [secret]
    for i in range(m-1):  #minimum shares to recompose
        polynomial.append(Mod(int_from_bytes2(urandom(16)), P))

    shards = {}
    for i in range(n):  #shares
        x = Mod(int_from_bytes2(urandom(16)), P)
        y = evaluate(polynomial, x)
        shards[i] = (x, y)

    for i in shards:
        f = open(f"secret{i+1}.txt", "w")
        f.write(str(shards[i]))
        f.close()

    #del shards[0] # for example 
    #del shards[1]

        

def recompose(files):
    print("\n Recomposing \n")

    retrieved_shards = {}
    for i in range(0,len(files)):
        data = str(open(files[i],"r").read())
        numbers = re.findall(r'\d+', data)
        retrieved_shards[i] = ( (Mod(int(numbers[0]),int(numbers[1]) )), (Mod(int(numbers[2]),int(numbers[3]) ))  )
    
    #print(retrieved_shards)

    retrieved = list(retrieved_shards.values())
    retrieved_secret = retrieve_original(retrieved, P)
    try:
     print("The message recomposed is: ", int_to_bytes(int(retrieved_secret)).decode("utf-8") + "\n")
    except:
        print("error: secret can't be decoded")
    


def run():
    if sys.argv[1] == "-split":
        n = int(sys.argv[2])
        m = int(sys.argv[3])
        file = sys.argv[4]
        split(n,m,file)

    elif sys.argv[1] == "-recompose":
        recompose(sys.argv[2:]) #only files
    else:
        print("\n Error: No command given, try -split or -recompose \n")



# Main
try:
  run()
except Exception as e:
    print("Error: can't run program, cause :", e)
