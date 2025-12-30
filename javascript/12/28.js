// SCREAMING_SNAKE_CASE

// Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

// The given variable names will be written in one of the following formats:

//     camelCase
//     PascalCase
//     snake_case
//     kebab-case

// In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

// To convert to SCREAMING_SNAKE_CASE:

//     Make all letters uppercase
//     Separate words with an underscore (_)

// 1. toScreamingSnakeCase("userEmail") should return "USER_EMAIL".
// 2. toScreamingSnakeCase("UserPassword") should return "USER_PASSWORD".
// 3. toScreamingSnakeCase("user_id") should return "USER_ID".
// 4. toScreamingSnakeCase("user-address") should return "USER_ADDRESS".
// 5. toScreamingSnakeCase("username") should return "USERNAME".

function toScreamingSnakeCase(variableName) {
    // Replace hyphens with underscores
    let result = variableName.replace(/-/g, '_')
    
    // Insert underscores before uppercase letters (for camelCase and PascalCase)
    result = result.replace(/([a-z])([A-Z])/g, '$1_$2')
    result = result.replace(/([A-Z])([A-Z][a-z])/g, '$1_$2')
    
    // Convert to uppercase
    result = result.toUpperCase()
    
    return result
}

// Test cases
console.log(toScreamingSnakeCase("userEmail")) 
console.log(toScreamingSnakeCase("UserPassword")) 
console.log(toScreamingSnakeCase("user_id")) 
console.log(toScreamingSnakeCase("user-address")) 
console.log(toScreamingSnakeCase("username")) 