def is_specialy_pythagorean_triplet(a:int,b:int,c:int,result:int) -> bool:
        if a**2 + b**2 == c**2 and a + b + c == result:
            return True
        return False

def find_specialy_thagorean() -> dict:
    for a in range(1,1000):
        for b in range (1,1000):
            c = 1000 - a - b
            if is_specialy_pythagorean_triplet(a,b,c,1000):
                return {'a':a,'b':b,'c':c}

print(find_specialy_thagorean())
