# 2026 Winter Games Day 15: Freestyle Skiing

# Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.

# A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.

#     The two words will be separated by a single space.

# Valid first words:
# "Misty"
# "Ghost"
# "Thunder"
# "Solar"
# "Sky"
# "Phantom"
# "Frozen"
# "Polar"

# Valid second words:
# "Twister"
# "Icequake"
# "Avalanche"
# "Vortex"
# "Snowstorm"
# "Frostbite"
# "Blizzard"
# "Shadow"
# Tests:

#     Waiting: 1. is_valid_trick("Polar Vortex") should return True.
#     Waiting: 2. is_valid_trick("Solar Icequake") should return True.
#     Waiting: 3. is_valid_trick("Thunder Blizzard") should return True.
#     Waiting: 4. is_valid_trick("Phantom Frostbite") should return True.
#     Waiting: 5. is_valid_trick("Ghost Avalanche") should return True.
#     Waiting: 6. is_valid_trick("Snowstorm Shadow") should return False.
#     Waiting: 7. is_valid_trick("Solar Sky") should return False.

def is_valid_trick(trick_name):
    first = [
        "Misty",
        "Ghost",
        "Thunder",
        "Solar",
        "Sky",
        "Phantom",
        "Frozen",
        "Polar",
    ]
    second = [
        "Twister",
        "Icequake",
        "Avalanche",
        "Vortex",
        "Snowstorm",
        "Frostbite",
        "Blizzard",
        "Shadow",
    ]
    return (trick_name.split()[0] in first) and (trick_name.split()[1] in second)


print(is_valid_trick("Polar Vortex"))
print(is_valid_trick("Solar Icequake"))
print(is_valid_trick("Thunder Blizzard"))
print(is_valid_trick("Phantom Frostbite"))
print(is_valid_trick("Ghost Avalanche"))
print(is_valid_trick("Snowstorm Shadow"))
print(is_valid_trick("Solar Sky"))