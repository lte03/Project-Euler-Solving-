from math import sqrt

def find_nth_prime(number:int) -> int:
    def is_prime(num:int) -> bool:
        if num < 2:
            return False
        for i in range(2,int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    count = 0
    i = 2
    while count != number:
        if is_prime(i):
            count += 1
        if count == number:
            break
        i += 1
    return i

print(find_nth_prime(10001))
