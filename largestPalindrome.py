# Find the largest palindrome made from the product of two 3-digit numbers.


def find_largest_palindrome():
    palindromes = []
    for x in range(100, 1000):
        for z in range(100, 1000):
            if check_palindrome(x*z):
                palindromes.append(x*z)
    palindromes.sort()
    print(palindromes[-1])


def check_palindrome(number):
    string_number = str(number)
    reversed_string = string_number[::-1]
    if string_number == reversed_string:
        return True
    else:
        return False


find_largest_palindrome()
