def is_prime(n):
    return all(n % i for i in range(2, n))

def process_item(x):
    while(not is_prime(x)):
      x += 1

    return x

def main():

    x= input("Enter number: ")
    print(process_item(int(x)))

if __name__ == '__main__':
     main()
