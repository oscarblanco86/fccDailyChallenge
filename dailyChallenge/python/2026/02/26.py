# Letter and Number Count

# Given a string, return a message with the count of how many letters and numbers it contains.

#     Letters are A-Z and a-z.
#     Numbers are 0-9.
#     Ignore all other characters.

# Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead of "1 numbers".
# Tests:

#     Waiting: 1. count_letters_and_numbers("helloworld123") should return "The string has 10 letters and 3 numbers.".
#     Waiting: 2. count_letters_and_numbers("Catch 22") should return "The string has 5 letters and 2 numbers.".
#     Waiting: 3. count_letters_and_numbers("A1!") should return "The string has 1 letter and 1 number.".
#     Waiting: 4. count_letters_and_numbers("12345") should return "The string has 0 letters and 5 numbers.".
#     Waiting: 5. count_letters_and_numbers("password") should return "The string has 8 letters and 0 numbers.".

import re

def count_letters_and_numbers(s):
    letters = 0
    numbers = 0 
    letters_text = ""
    numbers_text = ""
    
    for ch in s:
        if bool(re.search(r"[a-zA-Z]", ch)): 
            letters += 1
        if bool(re.search(r"[\d]", ch)): 
            numbers += 1
    
    if letters == 0:
        letters_text = "0 letters"
    elif letters == 1:
        letters_text = "1 letter"
    else:
        letters_text = str(letters) + " letters"

    if numbers == 0:
        numbers_text = "0 numbers"
    elif numbers == 1:
        numbers_text = "1 number"
    else:
        numbers_text = str(numbers) + " numbers"

    return f"The string has {letters_text} and {numbers_text}."

print(count_letters_and_numbers("helloworld123"))
print(count_letters_and_numbers("Catch 22"))
print(count_letters_and_numbers("A1!"))
print(count_letters_and_numbers("12345"))
print(count_letters_and_numbers("password"))

# Copilot:
# letters = len(re.findall(r"[a-zA-Z]", s))
# numbers = len(re.findall(r"\d", s))

# letters = sum(ch.isalpha() for ch in s)
# numbers = sum(ch.isdigit() for ch in s)



# import re

# def count_letters_and_numbers(s):
#     letters = len(re.findall(r"[a-zA-Z]", s))
#     numbers = len(re.findall(r"\d", s))

#     letters_text = f"{letters} letter" + ("" if letters == 1 else "s")
#     numbers_text = f"{numbers} number" + ("" if numbers == 1 else "s")

#     return f"The string has {letters_text} and {numbers_text}."
