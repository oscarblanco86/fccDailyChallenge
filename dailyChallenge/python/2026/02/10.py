# 2026 Winter Games Day 5: Cross-Country Skiing

# Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

#     Given times are strings in "H:MM:SS" format.
#     Given times will be in order from fastest to slowest.
#     The winners time (fastest time) should correspond to "0".
#     Each other time should show the time behind the winner, in the format "+M:SS".

# For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].

# Waiting: 1. get_relative_results(["1:25:32", "1:26:10", "1:27:05"]) should return ["0", "+0:38", "+1:33"].
# Waiting: 2. get_relative_results(["1:00:01", "1:00:05", "1:00:10"]) should return ["0", "+0:04", "+0:09"].
# Waiting: 3. get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]) should return ["0", "+0:17", "+0:42", "+2:05"].
# Waiting: 4. get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]) should return ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"].
# Waiting: 5. get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]) should return ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"].


def get_relative_results(results):
    time = []
    diff = ['0']
    for r in results:
        H, MM, SS = r.split(":")
        time.append(int(H) * 3600 + int(MM) * 60 + int(SS))
    for t in time[1:]:
        difference = t - time[0]
        diff.append(f'+{str(difference // 60)}:{str("{:02}".format(difference % 60))}')
    return diff


print(get_relative_results(["1:25:32", "1:26:10", "1:27:05"]))
print(get_relative_results(["1:00:00", "1:00:05", "1:00:10"]))
print(get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]))
print(get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]))
print(get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]))