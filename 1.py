def palindrome_check(num):
    n = str(num)
    return n == n[::-1]


num = 1001
if palindrome_check(num):
    print(f"This {num} is a palindrome")
else:
    print(f"This {num} is a not palindrome")
