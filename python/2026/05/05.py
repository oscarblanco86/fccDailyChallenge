# Narcissistic Number

# Given a positive integer, determine whether it is a narcissistic number.

#     A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.

# For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.
# Tests:

#     Waiting: 1. is_narcissistic(153) should return True.
#     Waiting: 2. is_narcissistic(154) should return False.
#     Waiting: 3. is_narcissistic(371) should return True.
#     Waiting: 4. is_narcissistic(512) should return False.
#     Waiting: 5. is_narcissistic(9) should return True.
#     Waiting: 6. is_narcissistic(11) should return False.
#     Waiting: 7. is_narcissistic(9474) should return True.
#     Waiting: 8. is_narcissistic(6549) should return False.

def is_narcissistic(n):
    num = str(n)
    exp = len(num)
    total = 0
    for chr in num:
        total += int(chr) ** exp
    return int(num) == total

print(is_narcissistic(153))
print(is_narcissistic(154))
print(is_narcissistic(371))
print(is_narcissistic(512))
print(is_narcissistic(9))
print(is_narcissistic(11))
print(is_narcissistic(9474))
print(is_narcissistic(6549))

# pythoninc 

# def is_narcissistic(n):
#     s = str(n)
#     p = len(s)
#     return sum(int(d)**p for d in s) == n
