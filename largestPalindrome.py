# Find the largest palindrome made from the product of two 3-digit numbers.


def find_largest_palindrome():
    highest_palindrome = 0
    for x in range(100, 1000):
        for z in range(100, 1000):
            prod = x * z
            if check_palindrome(prod):
                if prod > highest_palindrome:
                    highest_palindrome = prod
    print(highest_palindrome)


def check_palindrome(number):
    s = str(number)
    return s == s[::-1]


find_largest_palindrome()
