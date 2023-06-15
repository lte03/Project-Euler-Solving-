from math import sqrt

def sum_of_primes(limit:int) -> int:
    def is_prime(num:int) -> bool:
        if num < 2:
            return False
        for i in range(2,int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    result = 0
    for i in range(limit+1):
        if is_prime(i):
            result += i
    return result

print(sum_of_primes(2000000))
