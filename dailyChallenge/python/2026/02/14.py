# 2026 Winter Games Day 9: Skeleton

# Given a string representing the curves on a skeleton track, determine the difficulty of the track.

#     The given string will only consist of the letters:
#         "L" for a left turn
#         "R" for a right turn
#         "S" for a straight segment

#     Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

#     All other curves add 5 points each (all other "L" or "R" characters).

#     Straight segments add 0 points.

# The difficulty of the track is based on the total score. Return:

#     "Easy" if the total is 0 - 100
#     "Medium" if the total is 101-200
#     "Hard" if the total is over 200

# Tests:

#     Waiting: 1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
#     Waiting: 2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
#     Waiting: 3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
#     Waiting: 4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
#     Waiting: 5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
#     Waiting: 6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy".


def get_difficulty(track):
    points = 0
    prev = 'S'
    for ch in track:
        if ch in ['L', 'R']: points += 5
        if ch in ['L', 'R'] and prev in ['L', 'R'] and prev != ch: points += 10
        prev = ch    
    print(points)

    if points <= 100: return 'Easy'
    if 101 <= points <= 200: return 'Medium'
    return 'Hard'


print(get_difficulty("SLSLLSRRLSRLRL"))
print(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"))
print(get_difficulty("SRRRRLSLLRLRSSRLSRL"))
print(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"))
print(get_difficulty("SLLSSLRLSLSLRSLSSLRL"))
print(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"))