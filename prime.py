import math


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n != 2 and n % i == 0:
                return False
    return True


def prime_number_upto(n):
    arr = []
    for i in range(2, n + 1):
        if is_prime(i) == True:
            arr.append(i)
    return arr


data = 20328

print(is_prime(data))
print(prime_number_upto(data))
