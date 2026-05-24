# String Mirror

# Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

# Waiting: 1. mirror("freeCodeCamp") should return "freeCodeCamppmaCedoCeerf".
# Waiting: 2. mirror("RaceCar") should return "RaceCarraCecaR".
# Waiting: 3. mirror("helloworld") should return "helloworlddlrowolleh".
# Waiting: 4. mirror("The quick brown fox...") should return "The quick brown fox......xof nworb kciuq ehT".

def mirror(s):
    sr = []
    for ch in s:
        sr.insert(0,ch)
    return s + "".join(sr)

print(mirror("freeCodeCamp"))
print(mirror("RaceCar"))
print(mirror("helloworld"))
print(mirror("The quick brown fox..."))

# pythonic way 
# def mirror(s): return s + s[::-1]