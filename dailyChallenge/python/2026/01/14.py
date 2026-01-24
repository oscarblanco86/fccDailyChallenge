# Markdown Link Parser

# Given the string of a link in Markdown, return the equivalent HTML string.

# A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

# For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

# Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.



# 1. parse_link("[freeCodeCamp](https://freecodecamp.org/)") should return '<a href="https://freecodecamp.org/">freeCodeCamp</a>'.
# 2. parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)") should return '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>'.
# 3. parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)") should return '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>'.

def parse_link(markdown):
    name, link = markdown.strip("[)").split("](")
    return f'<a href="{link}">{name}</a>'

print(parse_link("[freeCodeCamp](https://freecodecamp.org/)"))
print(parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)"))
print(parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)"))

# copilots answer

# def parse_link(markdown):
#     name = markdown[1:markdown.index("]")]
#     link = markdown[markdown.index("(")+1 : markdown.rindex(")")]
#     return f'<a href="{link}">{name}</a>'
