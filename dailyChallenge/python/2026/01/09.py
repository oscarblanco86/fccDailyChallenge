# Circular Prime

# Given an integer, determine if it is a circular prime.

# A circular prime is an integer where all rotations of its digits are themselves prime.

# For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.



# 1. is_circular_prime(197) should return True.
# 2. is_circular_prime(23) should return False.
# 3. is_circular_prime(13) should return True.
# 4. is_circular_prime(89) should return False.
# 5. is_circular_prime(1193) should return True.

def is_circular_prime(n):
    modN = str(n)
    for i in str(n):
        modN = modN[1:] + i
        for j in range(2, int(modN) - 1):
            if int(modN) % j == 0: return False
    return True

print(is_circular_prime(197))
print(is_circular_prime(23))
print(is_circular_prime(13))
print(is_circular_prime(89))
print(is_circular_prime(1193))