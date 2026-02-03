# Bingo! Letter

# Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:
# Letter 	Number Range
# "B" 	1-15
# "I" 	16-30
# "N" 	31-45
# "G" 	46-60
# "O" 	61-75


# 1. get_bingo_letter(75) should return "O".
# 2. get_bingo_letter(54) should return "G".
# 3. get_bingo_letter(25) should return "I".
# 4. get_bingo_letter(38) should return "N".
# 5. get_bingo_letter(11) should return "B".

bingo = {
    "B": "1-15",
    "I": "16-30",
    "N": "31-45",
    "G": "46-60",
    "O": "61-75",
}

def get_bingo_letter(n):
    for letter, range_str in bingo.items():
        start, end = map(int, range_str.split('-'))
        if start <= n <= end:
            return letter
    return None

print(get_bingo_letter(75))
print(get_bingo_letter(54))
print(get_bingo_letter(25))
print(get_bingo_letter(38))
print(get_bingo_letter(11))