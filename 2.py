def sum_of_fibonacci(limit:int) -> int:
    result = 0
    f1 = 1
    f2 = 1
    while f1 + f2 < limit:
        temp = f1 + f2
        f2 = f1
        f1 = temp
        if f1 % 2 == 0:
            result += f1
    return result

print(sum_of_fibonacci(4000000))
