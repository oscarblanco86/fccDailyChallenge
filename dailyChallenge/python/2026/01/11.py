# Par for the Hole

# Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

# Return:

#     "Hole in one!" if it took one stroke.
#     "Eagle" if it took two strokes less than par.
#     "Birdie" if it took one stroke less than par.
#     "Par" if it took the same number of strokes as par.
#     "Bogey" if it took one stroke more than par.
#     "Double bogey" if took two strokes more than par.



# Waiting: 1. golf_score(3, 3) should return "Par".
# Waiting: 2. golf_score(4, 3) should return "Birdie".
# Waiting: 3. golf_score(3, 1) should return "Hole in one!".
# Waiting: 4. golf_score(5, 7) should return "Double bogey".
# Waiting: 5. golf_score(4, 5) should return "Bogey".
# Waiting: 6. golf_score(5, 3) should return "Eagle".

def golf_score(par, strokes):
    if strokes == 1: return "Hole in one!"
    if par - strokes == 2: return "Eagle"
    if par - strokes == 1: return "Birdie"
    if par == strokes: return "Par"
    if strokes - par == 1: return "Bogey" 
    if strokes - par == 2: return "Double bogey" 

print(golf_score(3, 3))
print(golf_score(4, 3))
print(golf_score(3, 1))
print(golf_score(5, 7))
print(golf_score(4, 5))
print(golf_score(5, 3))