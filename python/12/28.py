# SCREAMING_SNAKE_CASE

# Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

# The given variable names will be written in one of the following formats:

#     camelCase
#     PascalCase
#     snake_case
#     kebab-case

# In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

# To convert to SCREAMING_SNAKE_CASE:

#     Make all letters uppercase
#     Separate words with an underscore (_)

# to_screaming_snake_case("userEmail") should return "USER_EMAIL".
# to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
# to_screaming_snake_case("user_id") should return "USER_ID".
# to_screaming_snake_case("user-address") should return "USER_ADDRESS".
# to_screaming_snake_case("username") should return "USERNAME".
def to_screaming_snake_case(variable_name):
    import re
    
    # Replace hyphens with underscores
    variable_name = variable_name.replace('-', '_')
    
    # Insert underscores before uppercase letters (for camelCase and PascalCase)
    variable_name = re.sub(r'(?<!^)(?=[A-Z])', '_', variable_name)
    
    # Convert to uppercase
    screaming_snake_case = variable_name.upper()
    
    return screaming_snake_case

print(to_screaming_snake_case("userEmail"))     
print(to_screaming_snake_case("UserPassword"))   
print(to_screaming_snake_case("user_id"))        
print(to_screaming_snake_case("user-address"))   
print(to_screaming_snake_case("username"))       