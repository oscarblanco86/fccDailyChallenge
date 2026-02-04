# FizzBuzz Mini

# Given an integer, return a string based on the following rules:

#     If the number is divisible by 3, return "Fizz".
#     If the number is divisible by 5, return "Buzz".
#     If the number is divisible by both 3 and 5, return "FizzBuzz".
#     Otherwise, return the given number as a string.

# 1. fizz_buzz_mini(3) should return "Fizz".
# 2. fizz_buzz_mini(4) should return "4".
# 3. fizz_buzz_mini(35) should return "Buzz".
# 4. fizz_buzz_mini(75) should return "FizzBuzz".
# 5. fizz_buzz_mini(98) should return "98".

def fizz_buzz_mini(n):
    if (n % 3 == 0) and ( n % 5 == 0): return 'FizzBuzz'
    if (n % 3 == 0): return 'Fizz'
    if ( n % 5 == 0): return 'Buzz'
    return str(n)


print(fizz_buzz_mini(3))
print(fizz_buzz_mini(4)) 
print(fizz_buzz_mini(35)) 
print(fizz_buzz_mini(75)) 
print(fizz_buzz_mini(98)) 