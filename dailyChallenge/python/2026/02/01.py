# Digital Detox

# Given an array of your login logs, determine whether you have met your digital detox goal.

# Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

# You have met your digital detox goal if both of the following statements are true:

#     You logged in no more than once within any four-hour period.
#     You logged in no more than 2 times on any single day.

# 1. digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
# 2. digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]) should return False.
# 3. digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
# 4. digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]) should return False.
# 5. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) should return True.
# 6. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) should return False.

import datetime
# import time
def digital_detox(logs):
    dates = []
    times = []
    logs_a_day = 0
    for index, log in enumerate(logs):
        # print(datetime.datetime(log))
        curr_date, curr_time = log.split(' ')
        dates.append(curr_date)
        times.append(curr_time)
        year, month, day = curr_date.split('-')
        curr_hour, curr_minute, curr_second = curr_time.split(':')
        if index >= 1 and dates[index - 1] == curr_date:
            logs_a_day += 1
            if logs_a_day > 2:
                return False
            prev_date, prev_time = logs[index - 1].split(' ')
            # prev_year, prev_month, prev_day = prev_date.split('-')
            prev_hour, prev_minute, prev_second = prev_time.split(':')
            # curr_log = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
            # prev_log = datetime.datetime(int(prev_year), int(prev_month), int(prev_day), int(prev_hour), int(prev_minute), int(prev_second))
            print(datetime.time(int(prev_hour),int(prev_minute))-datetime(int(curr_hour,int(curr_minute),(curr_second)))
            # print(datetime.datetime(0,0,0,4,0,0))
            # if curr_log - prev_log < datetime.datetime(0,0,0,4,0,0):
            #     return False
    return True

    # print('date', dates)
    # print('time', times)
    return True

print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
