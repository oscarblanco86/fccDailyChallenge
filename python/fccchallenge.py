# def get_headings(csv):
#     newCsv = csv.split(",")
#     print(newCsv)
#     cleanNewCsv = []
#     for word in newCsv:
#         print(word.strip())
#         cleanNewCsv.append(word.strip())

#     return cleanNewCsv

# print(get_headings(("name,age,city")))
# print(get_headings(("first name,last name,phone")))
# print(get_headings(("username , email , signup date ")))

# def is_spam(number):
#     country, area, localNumber = number.split(" ")
#     cleanCountry = (country.replace("+", ""))
#     localArea, phone = localNumber.split("-")
#     cleanArea = int(area.replace("(", '').replace(")", ''))
#     cleanNumber = str(cleanArea) + str(localArea) + str(phone)
#     sumLocalArea = 0
#     count = 0
#     phoneNumberArray = []
#     if (len(cleanCountry) > 2) or (str(cleanCountry[0] )!= '0'): return True 
#     if (cleanArea < 200) or (cleanArea > 900): return True
#     i = 0
#     for i in range(len(localArea)):
#         sumLocalArea +=  int(localArea[i])
#         i += 1
#     i = 0
#     for i in range(len(phone)):
#         phoneNumberArray.append(int(phone[i]))
#         i += 1
#     i = 0
#     if (sumLocalArea in phoneNumberArray): return True
#     for i in range(len(cleanNumber) - 1):
#         if cleanNumber[i] == cleanNumber[i + 1]: count += 1 
#         else: count = 0
#         if count == 3: return True
#     return False

# print(is_spam("+0 (200) 234-0182") )
# print(is_spam("+091 (555) 309-1922"))
# print(is_spam("+1 (555) 435-4792"))
# print(is_spam("+0 (955) 234-4364"))
# print(is_spam("+0 (155) 131-6943"))
# print(is_spam("+0 (555) 135-0192"))
# print(is_spam("+0 (555) 564-1987"))
# print(is_spam("+00 (555) 234-0182") )

# def speeding(speeds, limit):
#     vehicles = 0
#     accum = 0
#     average = 0
#     for speed in speeds:
#         if speed > limit:
#             vehicles += 1 
#             accum += speed
#     if vehicles > 0:
#         average = accum / vehicles 
#         if average < 0:
#             average = 0
#         else:
#             average -= limit

#     return [vehicles, average]

# print(speeding([50, 60, 55], 60))
# print(speeding([58, 50, 60, 55], 55))
# print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
# print(speeding([100, 105, 95, 102], 100))
# print(speeding([40, 45, 44, 50, 112, 39], 55))

# def second_largest(arr):
#     newArr = list(set(arr))
#     newArr.sort()
#     print(newArr)
#     return newArr[-2]

# print(second_largest([1, 2, 3, 4]))
# print(second_largest([20, 139, 94, 67, 31]))
# print(second_largest([2, 3, 4, 6, 6]))
# print(second_largest([10, -17, 55.5, 44, 91, 0]))
# print(second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]))

# def is_perfect_square(n):
#     if n == 0:
#         return True
#     if n < 0:
#         return False
#     result = n ** 0.5
#     print(result)
#     if n % result != 0 :
#         return False
#     else:
#         return True

# print(is_perfect_square(9))
# print(is_perfect_square(49))
# print(is_perfect_square(1))
# print(is_perfect_square(2))
# print(is_perfect_square(99))
# print(is_perfect_square(-9))
# print(is_perfect_square(0))
# print(is_perfect_square(25281))

# def digits_or_letters(s):
#     digits = 0
#     letters = 0
#     for char in s:
#         if char.isnumeric(): 
#             digits += 1 
#         else: 
#             letters += 1
#     if digits > letters:
#         return "digits"
#     elif letters > digits:
#         return "letters"
#     else:
#         return "tie"


# digits_or_letters("abc123")
# digits_or_letters("a1b2c3d")
# digits_or_letters("1a2b3c4")
# digits_or_letters("abc123!@#DEF")
# digits_or_letters("H3110 W0R1D")
# digits_or_letters("P455W0RD")

# def number_of_videos(video_size, video_unit, drive_size, drive_unit):
#     def conversion(vSize, dSize, dUnit):
#         if (dUnit not in ["GB", "TB"]): return "Invalid drive unit"
#         if dUnit == "GB":
#             return int(dSize * 1000 / vSize)
#         return int(dSize * 1000000 / vSize)
        
#     if video_unit == "B": 
#         return conversion(video_size / 1000000, drive_size, drive_unit)
#     if video_unit == "KB": 
#         return conversion(video_size / 1000, drive_size, drive_unit)
#     if video_unit == "MB": 
#         return conversion(video_size , drive_size, drive_unit)
#     if video_unit == "GB": 
#         return conversion(video_size * 1000, drive_size, drive_unit)
#     return "Invalid video unit"

# print(number_of_videos(500, "MB", 100, "GB"))
# print(number_of_videos(1, "TB", 10, "TB"))
# print(number_of_videos(2000, "MB", 100000, "MB"))
# print(number_of_videos(500000, "KB", 2, "TB"))
# print(number_of_videos(1.5, "GB", 2.2, "TB"))

# def number_of_files(file_size, file_unit, drive_size_gb):
#     if file_unit == "B": return int(drive_size_gb * 1000000000 / file_size)
#     if file_unit == "KB": return int(drive_size_gb * 1000000 / file_size)
#     if file_unit == "MB": return int(drive_size_gb * 1000 / file_size)

# print(number_of_files(500, "KB", 1))
# print(number_of_files(4096, "B", 1.5))
# print(number_of_files(220.5, "KB", 100))

# def cost_to_fill(tank_size, fuel_level, price_per_gallon):
#     cost = round((tank_size - fuel_level) * price_per_gallon, 2)
#     return f"${cost:.2f}"
    
    
# print(cost_to_fill(12, 12, 4.99))
# print(cost_to_fill(18, 9, 3.25))
# print(cost_to_fill(15, 9.5, 3.98))
# print(cost_to_fill(20, 0, 4.00))


# def generate_slug(str):
#     for ch in ["?", "*", "^", "]", "[", "!", "#", "-", "%"]:
#         str = str.replace(ch, '')
#     phrase = str.casefold().strip().replace("  ", "%20").replace(" ", "%20")
#     return phrase
# print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))

# def capitalize(s):
#     result = []
#     capitalize_next = True  # start of first sentence

#     for ch in s:
#         if capitalize_next and ch.isalpha():
#             result.append(ch.upper())
#             capitalize_next = False
#         else:
#             result.append(ch)

#         if ch in ".!?":
#             capitalize_next = True
#     return "".join(result)

# capitalize("there's a space before this period . why is there a space before that period ?")

# def adjust_thermostat(temp, target):
#     return "heat" if temp < target else ("cool" if temp > target else "hold")


# def get_words(paragraph):
#     for char in '.,!?":;()[]{}':
#         paragraph = paragraph.replace(char, '')

#     word_list = paragraph.lower().split(" ")

#     word_count = {}
#     for word in word_list:
#         word_count[word] = word_count.get(word, 0) + 1

#     sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
#     return [word for word, count in sorted_words[:3]]

# print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))

# print(get_words("I like coding. I like testing. I love debugging!"))

# def find_missing_numbers(arr):
#     result = []
#     n = 1
#     for n in range(min(arr),max(arr)):
#         if n not in arr:
#             result.append(n)
#     print(result)
#     return result

# print(find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]))

# def too_much_screen_time(hours):
#     for x in hours:
#         if x >= 10:
#             return True
#     i = 0
#     while i <= (len(hours) - 3):
#         avg = (hours[i] + hours[i+1] + hours[i+2]) / 3
#         i += 1
#         if avg > 8:
#             return True
#     avg = 0
#     for y in hours:
#         avg += y
#     print(avg/len(hours))
#     if (avg / len(hours)) > 6:
#         return True

# print(too_much_screen_time([3, 9, 4, 8, 5, 7, 6]))
