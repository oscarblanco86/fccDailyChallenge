# Deepest Brackets

# Given a string containing balanced brackets, return the content of the deepest nested brackets.

#     Brackets can be any of the three types: (), [], and {}.
#     The input will always have a single deepest group.

# For example, given "(hello (world))", return "world".
# Tests:

#     Waiting: 1. get_deepest_brackets("(hello (world))") should return "world".
#     Waiting: 2. get_deepest_brackets("[outer [inner] outer]") should return "inner".
#     Waiting: 3. get_deepest_brackets("{a{b}c{d{e}f}g}") should return "e".
#     Waiting: 4. get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]") should return "fox".
#     Waiting: 5. get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p") should return "C".


def get_deepest_brackets(s):
    depth = 0
    content = ''
    content_depth = 0
    for ch in s:
        if ch in ["(","[","{"]:
            depth += 1
            if depth > content_depth: 
                content = ''
                content_depth = depth
            continue
        if ch in [")","]","}"]:
            depth -= 1
            continue
        if content_depth == depth:
            content += ch
            
    return content



print(get_deepest_brackets("(hello (world))"))
print(get_deepest_brackets("[outer [inner] outer]"))
print(get_deepest_brackets("{a{b}c{d{e}f}g}"))
print(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"))
print(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"))
