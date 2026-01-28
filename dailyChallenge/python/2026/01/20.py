# Consonant Case

# Given a string representing a variable name, convert it to consonant case using the following rules:

#     All consonants should be converted to uppercase.
#     All vowels (a, e, i, o, u in any case) should be converted to lowercase.
#     All hyphens (-) should be converted to underscores (_).


# 1. to_consonant_case("helloworld") should return "HeLLoWoRLD".
# 2. to_consonant_case("HELLOWORLD") should return "HeLLoWoRLD".
# 3. to_consonant_case("_hElLO-WOrlD-") should return "_HeLLo_WoRLD_".
# 4. to_consonant_case("_~-generic_~-variable_~-name_~-here-~_") should return "_~_GeNeRiC_~_VaRiaBLe_~_NaMe_~_HeRe_~_".


def to_consonant_case(s):
    uppercased_string = ""
    for ch in s:
        if ch == '-':
            uppercased_string += '_'
        elif ch not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            uppercased_string += ch.upper()
        else:
            uppercased_string += ch.lower()
    return uppercased_string


print(to_consonant_case("helloworld"))
print(to_consonant_case("HELLOWORLD"))
print(to_consonant_case("_hElLO-WOrlD-"))
print(to_consonant_case("_~-generic_~-variable_~-name_~-here-~_"))

#pythonic answer:
# def to_consonant_case(s):
#     vowels = {"a", "e", "i", "o", "u"}
#     result = []

#     for ch in s:
#         if ch == "-":
#             result.append("_")
#         elif ch.lower() in vowels:
#             result.append(ch.lower())
#         else:
#             result.append(ch.upper())

#     return "".join(result)
