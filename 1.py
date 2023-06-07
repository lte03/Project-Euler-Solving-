def multiples_3_and_5(limit:int) -> int:
    result = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

print(multiples_3_and_5(1000))
