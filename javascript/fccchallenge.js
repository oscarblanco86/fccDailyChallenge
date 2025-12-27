// function getHeadings(csv) {
//   const newCsv = csv.split(",")
//   const cleanNewCsv = newCsv.map((item) => item.trim())
//   return cleanNewCsv;
// }

// console.log(getHeadings(("name,age,city")))
// console.log(getHeadings(("first name,last name,phone")))
// console.log(getHeadings(("username , email , signup date ")))

// function isSpam(number) { 
//     const [country, area, localNumber] = number.split(" ") 
//     const cleanArea = area.replace(['('],'').replace([')'],'') 
//     const [localArea, phoneNumber] = localNumber.split("-") 
//     const cleanNumber = cleanArea + localArea + phoneNumber 
//     console.log(country.length) 
//     console.log(cleanNumber) 
//     let count = 0 
//     let sumLocalArea = 0 
//     let phoneNumberArray = [] 
//     if (country.length > 3 || country[1] != '0') return true 
//     if (cleanArea < 200 || cleanArea > 900) return true 
//     for (let i = 0; i < localArea.length; i++) { 
//         sumLocalArea += Number(localArea[i]) 
//     } 
//     for (let i = 0; i < phoneNumber.length; i++) { 
//         phoneNumberArray.push(Number(phoneNumber[i])) 
//     } 
//     if (phoneNumberArray.includes(sumLocalArea)) return true 
//     for (let i = 0; i < cleanNumber.length; i++) { 
//         if (cleanNumber[i] == cleanNumber[i + 1]) {count++} else {count=0} 
//         if (count === 3) return true 
//     } 
//     return false
// }


//// Copilot refactor
// function isSpam(number) {
//   const [country, area, localNumber] = number.split(" ");
//   const cleanCountry = country.replace('+', '');
//   const cleanArea = area.replace('(', '').replace(')', '');
//   const [localArea, phoneNumber] = localNumber.split("-");
//   const cleanNumber = cleanArea + localArea + phoneNumber;

//   // Country code check
//   if (cleanCountry.length > 2 || cleanCountry[0] !== '0') return true;

//   // Area code check
//   const areaNum = Number(cleanArea);
//   if (areaNum < 200 || areaNum > 900) return true;

//   // Local sum check
//   const sumLocalArea = [...localArea].reduce((sum, d) => sum + Number(d), 0);
//   if (phoneNumber.includes(sumLocalArea.toString())) return true;

//   // Repeated digit check
//   let count = 0;
//   for (let i = 0; i < cleanNumber.length; i++) {
//     if (cleanNumber[i] === cleanNumber[i + 1]) {
//       count++;
//       if (count >= 3) return true; // 4 in a row
//     } else {
//       count = 0;
//     }
//   }

//   return false;
// }


console.log(isSpam("+0 (200) 234-0182") )
console.log(isSpam("+091 (555) 309-1922"))
console.log(isSpam("+1 (555) 435-4792"))
console.log(isSpam("+0 (955) 234-4364"))
console.log(isSpam("+0 (155) 131-6943"))
console.log(isSpam("+0 (555) 135-0192"))
console.log(isSpam("+0 (555) 564-1987"))
console.log(isSpam("+00 (555) 234-0182") )

// function speeding(speeds, limit) {
//   let vehicles = 0
//   let accum = 0
//   let average = 0
//   speeds.map(speed => {
//     if (speed > limit) {
//       vehicles += 1
//       accum += speed
//     }
//   })
//   if (vehicles > 0) {
//     average = accum / vehicles
//     if (vehicles < 0) {
//       average = 0
//     } else {
//       average -= limit
//     }
//   }
//   return [vehicles, average];
// }

// console.log(speeding([50, 60, 55], 60))
// console.log(speeding([58, 50, 60, 55], 55))
// console.log(speeding([61, 81, 74, 88, 65, 71, 68], 70))
// console.log(speeding([100, 105, 95, 102], 100))
// console.log(speeding([40, 45, 44, 50, 112, 39], 55))

// function secondLargest(arr) {
//   newArr = [...new Set(arr)]
//   newArr.sort((a, b) => a - b)
//   return newArr.at(-2);
// }

// console.log(secondLargest([1, 2, 3, 4]))
// console.log(secondLargest([20, 139, 94, 67, 31]))
// console.log(secondLargest([2, 3, 4, 6, 6]))
// console.log(secondLargest([10, -17, 55.5, 44, 91, 0]))
// console.log(secondLargest([1, 0, -1, 0, 1, 0, -1, 1, 0]))

// function isPerfectSquare(n) {
//   const result = Math.sqrt(n) 
//   if (Number.isInteger(result)) {
//     return true
//   } else 
//     return false
//   }
// }


// console.log(isPerfectSquare(9))
// console.log(isPerfectSquare(49))
// console.log(isPerfectSquare(1))
// console.log(isPerfectSquare(2))
// console.log(isPerfectSquare(99))
// console.log(isPerfectSquare(-9))
// console.log(isPerfectSquare(0))
// console.log(isPerfectSquare(25281))


// function isMirror(str1, str2) {
//   const clean1 = str1.replace(['-','!'], ' ').replace(/[^a-z0-9]/g, '')
//   const clean2 = str2.replace(['-','!'], ' ').replace(/[^a-z0-9]/g, '')
//   console.log(clean1, clean2)
//   if (clean1.length != clean2.length) return false
//   for (let i = 0; i < clean1.length ; i++) {
//     console.log(clean1[i], clean2[clean1.length - i - 1])
//     console.log(clean1[i] != clean2[clean1.length - i -1])
//     if (clean1[i] != clean2[clean1.length - i - 1]) {
//       return false
//     }
//   }
//   return true
// }
// console.log(isMirror("helloworld", "helloworld"))
// console.log(isMirror("Hello World", "dlroW olleH"))
// console.log(isMirror("RaceCar", "raCecaR"))
// console.log(isMirror("RaceCar", "RaceCar"))
// console.log(isMirror("Mirror", "rorrim"))
// console.log(isMirror("Hello World", "dlroW-olleH"))
// console.log(isMirror("Hello World", "!dlroW !olleH"))

// function digitsOrLetters(str) {
//   let letters = 0
//   let digits = 0
//   for (let i = 0; i< str.length; i++ ) {
//     // console.log(str[i], isFinite(str[i]))
//     if (isFinite(str[i])) {digits += 1} else {letters += 1}
//   }
//   console.log(digits, letters)
//   if (letters > digits) return "letters" 
//   if (digits > letters) return "digits"
//   return "tie"
// }

// console.log(digitsOrLetters("abc123"))
// console.log(digitsOrLetters("a1b2c3d"))
// console.log(digitsOrLetters("1a2b3c4"))
// console.log(digitsOrLetters("abc123!@#DEF"))
// console.log(digitsOrLetters("H3110 W0R1D"))
// console.log(digitsOrLetters("P455W0RD"))


// function numberOfVideos(videoSize, videoUnit, driveSize, driveUnit) {
//   function conversion(vSize, dSize, dUnit) {
//     if (dUnit != "GB" && dUnit != "TB") 
//       return "Invalid drive unit"
//     if (dUnit == "GB") 
//       return Math.floor(dSize * 1000 / vSize)
//     return Math.floor(dSize * 1000000 / vSize)
//    }
//   if (videoUnit === "B") 
//     return (conversion(videoSize / 1000000, driveSize, driveUnit))
//   if (videoUnit === "KB") 
//     return (conversion(videoSize / 1000, driveSize, driveUnit))
//   if (videoUnit === "MB") 
//     return (conversion(videoSize, driveSize, driveUnit))
//   if (videoUnit === "GB") 
//     return (conversion(videoSize * 1000, driveSize, driveUnit))
//   return "Invalid video unit";
// }

// console.log(numberOfVideos(500, "MB", 100, "GB"))
// console.log(numberOfVideos(1, "TB", 10, "TB"))
// console.log(numberOfVideos(2000, "MB", 100000, "MB"))
// console.log(numberOfVideos(500000, "KB", 2, "TB"))
// console.log(numberOfVideos(1.5, "GB", 2.2, "TB"))


// function numberOfFiles(fileSize, fileUnit, driveSizeGb) {
//   if (fileUnit === "B") return Math.floor(driveSizeGb * 1000000000 / fileSize)
//   if (fileUnit === "KB") return Math.floor(driveSizeGb * 1000000 / fileSize)
//   if (fileUnit === "MB") return Math.floor(driveSizeGb * 1000 / fileSize)
//   return fileSize;
// }

// console.log(numberOfFiles(500, "KB", 1))
// console.log(numberOfFiles(4096, "B", 1.5))
// console.log(numberOfFiles(220.5, "KB", 100))

// function costToFill(tankSize, fuelLevel, pricePerGallon) {
//   const cost = (tankSize - fuelLevel) * pricePerGallon;
//   return "$" + cost.toFixed(2);
// }

// console.log(costToFill(12, 12, 4.99))
// console.log(costToFill(18, 9, 3.25))

// console.log(costToFill(15, 9.5, 3.98))
// console.log(costToFill(20, 0, 4.00))

// function generateSlug(str) {
//   return str
//     .toLowerCase()
//     .trim()
//     .replace(/[^a-z0-9 ]/g, '') 
//     .replace(/  /g, '%20')
//     .replace(/ /g, '%20');
// }

// console.log((generateSlug("  ?H^3-1*1]0! W[0%R#1]D  ") === "h3110%20w0r1d"))
// console.log(generateSlug("  ?H^3-1*1]0! W[0%R#1]D  "))

// function capitalize(paragraph) {
//   let result = "";
//   let capitalizeNext = true; // start of first sentence

//   for (let ch of paragraph) {
//     if (capitalizeNext && /[a-z]/.test(ch)) {
//       result += ch.toUpperCase();
//       capitalizeNext = false;
//     } else {
//       result += ch;
//     }

//     // If we hit a sentence-ending punctuation, the next letter should be capitalized
//     if (ch === "." || ch === "!" || ch === "?") {
//       capitalizeNext = true;
//     }
//   }

//   return result
// }

// capitalize("there's a space before this period . why is there a space before that period ?")

// function adjustThermostat(temp, target) {
  
//   return (temp > target) ? "cool" : (temp < target) ? "heat" : "hold";
// }

// function getWords(paragraph) {
//   let plc = paragraph
//     .toLocaleLowerCase()
//     .replace(/["',.]/g, '')
//     .split(" ")
//   let wcount = {}
//   for (const word of plc) {
//     if (word in wcount) wcount[word] +=1
//     if (!(word in wcount)) wcount[word] =1
//   }
//   const topThree = Object.entries(wcount)
//     .sort((a, b) => b[1] - a[1]) // sort by frequency
//     .slice(0, 3)
//     .map(([word]) => word)
//   return topThree
// }

// console.log(
//   getWords("I like coding. I like testing. I love debugging!")
// )

// function findMissingNumbers(arr) {
//   let arrSorted = arr.toSorted((a, b) => a - b)
//   let min = arrSorted[0]
//   let max = arrSorted[arrSorted.length - 1]
//   let newArr = []
//   for (let i = 1; i <= max; i++) {
//     console.log(i)
//     if (!arrSorted.includes(i)) newArr.push(i) 
//   }

//   console.log(arrSorted)
// console.log(newArr)
//   return newArr;
// }
// console.log(
//     findMissingNumbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4])
// )




// function tooMuchScreenTime(hours) {

//   for (let i = 0; (i - 3) <= hours.length; i++ ) {
//     let avg = (hours[i] + hours[i + 1] + hours[i + 2]) / 3
//     console.log(avg)
//     if (avg > 8) return true
//   }
//   if ((hours.reduce((a, b) => a + b) / hours.length >= 8)) return true 
//   if ((hours.reduce((a, b) => a + b) / hours.length >= 6) && (hours.length >=7)) return true 
//   return hours.some(h => h >= 10)}