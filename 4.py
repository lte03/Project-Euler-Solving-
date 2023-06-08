def ProductOfPalindromeFor3_digits() -> int:
    def isPalindrome(number:int) -> bool:
        original_number = number
        reversed_number = 0
        while number > 0:
            digit = number % 10
            reversed_number = (reversed_number * 10) + digit
            number = number // 10
        if original_number == reversed_number:
            return True
        else:
            return False

    largest_palindrome = 0

    for i in range(1000, 99, -1):
        for j in range(i, 99, -1):
            if isPalindrome(i * j):
                product = i * j
                if product > largest_palindrome:
                    largest_palindrome = product

    return largest_palindrome

print(ProductOfPalindromeFor3_digits())
