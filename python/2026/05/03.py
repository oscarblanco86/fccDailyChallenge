# Good Day

# Given a time string in "HH:MM" format (24-hour clock), return:

#     "Good morning" for times 05:00 to 11:59
#     "Good afternoon" for times 12:00 to 17:59
#     "Good evening" for times 18:00 to 21:59
#     "Good night" for times 22:00 to 04:59

# Tests:

#     Waiting: 1. get_greeting("06:30") should return "Good morning".
#     Waiting: 2. get_greeting("12:00") should return "Good afternoon".
#     Waiting: 3. get_greeting("21:59") should return "Good evening".
#     Waiting: 4. get_greeting("00:01") should return "Good night".
#     Waiting: 5. get_greeting("11:30") should return "Good morning".

greets = {
    "Good morning": "05:00 to 11:59",
    "Good afternoon": "12:00 to 17:59",
    "Good evening": "18:00 to 21:59",
    "Good night": "22:00 to 23:59",
    "Good night": "00:00 to 04:59",
}
def get_greeting(s):
    HH, MM = s.split(":")
    greet_time = int(HH) * 60 + int(MM)
    for greet, times in greets.items():
        starting, ending = times.split(" to ")
        starting_hh, starting_mm = starting.split(":")
        starting_time = int(starting_hh) * 60 + int(starting_mm)
        ending_hh, ending_mm = ending.split(":")
        ending_time = int(ending_hh) * 60 + int(ending_mm)
        if starting_time <= greet_time <= ending_time:
            return greet
        
# Pythonic answer
# greets = {
#     "Good morning": "05:00 to 11:59",
#     "Good afternoon": "12:00 to 17:59",
#     "Good evening": "18:00 to 21:59",
#     "Good night 1": "22:00 to 23:59",
#     "Good night 2": "00:00 to 04:59",
# }

# def get_greeting(s):
#     HH, MM = s.split(":")
#     greet_time = int(HH) * 60 + int(MM)

#     for greet, times in greets.items():
#         start, end = times.split(" to ")
#         sh, sm = map(int, start.split(":"))
#         eh, em = map(int, end.split(":"))
#         start_m = sh * 60 + sm
#         end_m = eh * 60 + em

#         if start_m <= greet_time <= end_m:
#             return "Good night" if "night" in greet else greet


print(get_greeting("06:30"))
print(get_greeting("12:00"))
print(get_greeting("21:59"))
print(get_greeting("00:01"))
print(get_greeting("11:30"))