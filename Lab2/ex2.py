
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
        
def prime_in_list(list):  
    prime_list = [] 
    for i in list:     
        if is_prime(i):
            prime_list.append(i)
   
    return prime_list

print(prime_in_list([1,2,3,4,5,6,7,8,9,10,11,12,13]))