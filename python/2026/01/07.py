# Markdown Unordered List Parser

# Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

# An unordered list consists of one or more list items. A valid list item appears on its own line and:

#     Starts with a dash ("-"), followed by
#     At least one space, and then
#     The list item text.

# The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

# Wrap each list item in HTML li tags, and the whole list of items in ul tags.

# For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>".

# Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.


# 1. parse_unordered_list("- Item A\n- Item B") should return "<ul><li>Item A</li><li>Item B</li></ul>".
# 2. parse_unordered_list("-  JavaScript\n-  Python") should return "<ul><li>JavaScript</li><li>Python</li></ul>".
# 3. parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla") should return "<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>".
# 4. parse_unordered_list("- A-1\n- A-2\n- B-1") should return "<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>".

# def parse_unordered_list(markdown):
#     result = f"<ul>{
#         markdown
#         .replace("-  ", "<li>")
#         .replace("- ", "<li>")
#         .replace("\n", "</li>")
#         }</li></ul>"
#     return result

def parse_unordered_list(markdown: str) -> str:
    items = []

    for line in markdown.split("\n"):
        # Remove the leading "-" and any spaces after it
        # Assumes input is valid as per the problem statement
        text = line[1:].lstrip()  # skip the "-" then strip spaces
        print(text)
        items.append(f"<li>{text}</li>")

    return "<ul>" + "".join(items) + "</ul>"


print(parse_unordered_list("- Item A\n- Item B"))
print(parse_unordered_list("-  JavaScript\n-  Python"))
print(parse_unordered_list("- 2 C Flour\n- 1/2 C Sugar\n- 1 Tsp Vanilla"))
print(parse_unordered_list("- A-1\n- A-2\n- B-1"))


<ul><li>Item A</li><li>Item B</li></ul>".
<ul><li>Item A</li><li>Item B</li></ul>
<ul><li>Item A</li><li>Item B</li></ul>
<ul><li>JavaScript</li><li>Python</li></ul>".
<ul><li>JavaScript</li><li>Python</li></ul>
<ul><li>JavaScript</li><li>Python</li></ul>
<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>".
<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>
<ul><li>2 C Flour</li><li>1/2 C Sugar</li><li>1 Tsp Vanilla</li></ul>
<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>".
<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>
<ul><li>A-1</li><li>A-2</li><li>B-1</li></ul>
