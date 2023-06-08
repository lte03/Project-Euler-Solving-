def calc_sum_of_squares(number:int) -> int:
    result = 0
    for i in range(number + 1):
        result += i**2
    return result

def calc_square_of_sum(number:int) -> int:
    result = 0
    for i in range(number + 1):
        result += i
    return result ** 2

def sub(number1:int,number2:int) -> int:
    return number1 - number2

print(sub(calc_square_of_sum(100),calc_sum_of_squares(100)))