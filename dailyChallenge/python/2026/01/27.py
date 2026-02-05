# Odd or Even Day

# Given a timestamp (number of milliseconds since the Unix epoch), return:

#     "odd" if the day of the month for that timestamp is odd.
#     "even" if the day of the month for that timestamp is even.

# For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.


# 1. odd_or_even_day(1769472000000) should return "odd".
# 2. odd_or_even_day(1769444440000) should return "even".
# 3. odd_or_even_day(6739456780000) should return "odd".
# 4. odd_or_even_day(1) should return "odd".
# 5. odd_or_even_day(86400000) should return "even".

from datetime import datetime

def odd_or_even_day(timestamp):
    dt = datetime.utcfromtimestamp(timestamp / 1000)
    print(dt)
    return "odd" if dt.day % 2 else "even"

print(odd_or_even_day(1769472000000))
print(odd_or_even_day(1769444440000))
print(odd_or_even_day(6739456780000))
print(odd_or_even_day(1))
print(odd_or_even_day(86400000))