// Hex Validator

// Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

//     Start with a #, and
//     be followed by either 3 or 6 hexadecimal characters.

// Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).


// 1. isValidHex("#123") should return true.
// 2. isValidHex("#123abc") should return true.
// 3. isValidHex("#ABCDEF") should return true.
// 4. isValidHex("#0a1B2c") should return true.
// 5. isValidHex("#12G") should return false.
// 6. isValidHex("#1234567") should return false.
// 7. isValidHex("#12 3") should return false.
// 8. isValidHex("fff") should return false.

function isValidHex(str) {
    if (str.charAt(0) !== "#") return false

    if (str.length !== 4 && str.length !== 7) return false

    const valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for (let ch of str.slice(1)) {   // skip the #
        if (!valid.includes(ch.toLowerCase())) return false
    }

    return true
}

console.log(isValidHex("#123"))
console.log(isValidHex("#123abc"))
console.log(isValidHex("#ABCDEF"))
console.log(isValidHex("#0a1B2c"))
console.log(isValidHex("#12G"))
console.log(isValidHex("#1234567"))
console.log(isValidHex("#12 3"))
console.log(isValidHex("fff"))