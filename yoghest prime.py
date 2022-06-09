# yoghest prime
import functools
import math


@functools.lru_cache(maxsize=2000)
def isprime(prime_no):
    if prime_no == 1:
        return False
    for i in range(2, math.floor(math.sqrt(prime_no))+1):
        if (prime_no % i == 0):
            return False
    return True


def total_prime(a, b, k):
    if a > b or a < 1 or a > 1000000 or b < 1 or b > 1000000:
        return -1
    count, answer = 0, 0
    for i in range(a, b+1):
        answer = i
        if isprime(i):
            count += 1
        if count == k:
            break

    if count != k:
        return -1
    else:
        return answer


if __name__ == "__main__":
    #     n = int(input())
    for i in range(int(input())):
        a = input().split(" ")
        print(total_prime(int(a[0]), int(a[1]), int(a[2])))
