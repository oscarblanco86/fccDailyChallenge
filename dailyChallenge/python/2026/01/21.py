# Markdown Inline Code Parser

# Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

# Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

# Return the given string with all code blocks converted to HTML code tags.

# For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

# 1. parse_inline_code("Use `let` to declare the variable.") should return "Use <code>let</code> to declare the variable.".
# 2. parse_inline_code("Use `let` or `const` to declare a variable.") should return "Use <code>let</code> or <code>const</code> to declare a variable.".
# 3. parse_inline_code("Run `npm install` then `npm start`.") should return "Run <code>npm install</code> then <code>npm start</code>.".


def parse_inline_code(markdown):
    close_code = False
    markdown_corrected = []
    for ch in markdown:
        if ch == '`':
            if close_code:
                close_code = False
                markdown_corrected.append('</code>')
            else:
                close_code = True
                markdown_corrected.append('<code>')
        else:
            markdown_corrected.append(ch)
    return "".join(markdown_corrected)


print(parse_inline_code("Use `let` to declare the variable."))
print(parse_inline_code("Use `let` or `const` to declare a variable."))
print(parse_inline_code("Run `npm install` then `npm start`."))

# Pythonic way
# def parse_inline_code(markdown):
#     in_code = False
#     result = []

#     for ch in markdown:
#         if ch == '`':
#             if in_code:
#                 result.append('</code>')
#             else:
#                 result.append('<code>')
#             in_code = not in_code
#         else:
#             result.append(ch)

#     return "".join(result)
