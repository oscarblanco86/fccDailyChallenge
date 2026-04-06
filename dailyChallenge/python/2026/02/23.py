# Blood Type Compatibility

# Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

# Each blood type consists of:

#     A letter: "A", "B", "AB", or "O"
#     And an Rh factor: "+" or "-"

# Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

# Letter Rules:

#     "O" can donate to other letter type.
#     "A" can donate to "A" and "AB".
#     "B" can donate to "B" and "AB".
#     "AB" can donate only to "AB".

# Rh Rules:

#     Negative ("-") can donate to both "-" and "+".
#     Positive ("+") can donate only to "+".

# Both letter and Rh rule must pass for a donor to be able to donate to the recipient.

    # Waiting: 1. can_donate("B+", "B+") should return True.
    # Waiting: 2. can_donate("O-", "AB-") should return True.
    # Waiting: 3. can_donate("O+", "A-") should return False.
    # Waiting: 4. can_donate("A+", "AB+") should return True.
    # Waiting: 5. can_donate("A-", "B-") should return False.
    # Waiting: 6. can_donate("B-", "AB+") should return True.
    # Waiting: 7. can_donate("B-", "A+") should return False.
    # Waiting: 8. can_donate("O-", "O+") should return True.
    # Waiting: 9. can_donate("O+", "O-") should return False.
    # Waiting: 10. can_donate("AB+", "AB-") should return False.

def can_donate(donor, recipient):
    can_donate_to = {
        "O": ["A", "B", "AB", "O"],
        "A": ["A", "AB"],
        "B": ["B", "AB"],
        "AB": ["AB"]
    }

    if (donor[-1] == "-") or (donor[-1] == recipient[-1]):
        if recipient[:-1] in can_donate_to[donor[:-1]]:
            return True
    return False


print(can_donate("B+", "B+"))
print(can_donate("O-", "AB-"))
print(can_donate("O+", "A-"))
print(can_donate("A+", "AB+"))
print(can_donate("A-", "B-"))
print(can_donate("B-", "AB+"))
print(can_donate("B-", "A+"))
print(can_donate("O-", "O+"))
print(can_donate("O+", "O-"))
print(can_donate("AB+", "AB-")) 