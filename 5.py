def EKOK_to_N(n:int) -> int:
    def Ebob(num1:int,num2:int):
        while num1 % num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num2
    def Ekok(num1:int,num2:int) -> int:
        return num1 * num2 / Ebob(num1,num2)
    ekok = 1
    for i in range(1,n+1):
        ekok = Ekok(ekok,i)
    return ekok

print(EKOK_to_N(20))
