# Anagram Groups

# Given an array of words, return a 2d array of the words grouped into anagrams.

#     Words are anagrams if they contain the same letters in any order.
#     Each word belongs to exactly one group.
#     Return order doesn't matter.

# For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].
# Tests:

# 1. group_anagrams(["listen", "silent", "hello", "enlist", "world"]) should return [["listen", "silent", "enlist"], ["hello"], ["world"]].
# 2. group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) should return [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]].
# 3. group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]) should return [["acre", "care", "race"], ["evil", "live", "veil", "vile"], ["opts", "post", "pots", "spot", "stop", "tops"]].
# 4. group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]) should return [["alerting", "integral", "relating", "triangle"], ["algorithms", "logarithms"], ["auctioned", "cautioned", "education"]].


def group_anagrams(words):
    anagram_word_list = {}
    for word in words:
        if anagram_word_list.get("".join(sorted(word))) == None:
            anagram_word_list["".join(sorted(word))] = [word]
        else:
            anagram_word_list["".join(sorted(word))].append(word)
        
    return [values for values in anagram_word_list.values()] 


# copilot pythonic solution:
# def group_anagrams(words):
#     groups = {}
#     for word in words:
#         key = "".join(sorted(word))
#         groups.setdefault(key, []).append(word)
#     return [sorted(g) for g in groups.values()]


print(group_anagrams(["listen", "silent", "hello", "enlist", "world"]))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]))
print(group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]))