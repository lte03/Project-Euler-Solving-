def largest_prime_factor(number:int):
    asal = 2
    while number > 1:
        if number % asal == 0:
            number //= asal
        else:
            asal += 1
    return asal

print(largest_prime_factor(600851475143))
