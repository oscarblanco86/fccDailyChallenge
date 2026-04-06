# Business Day Count

# Given a start date and an end date, return the number of business days between the two.

#     Given dates are in the format "YYYY-MM-DD".
#     Weekdays are business days (Monday through Friday).
#     Weekends are not business days (Saturday and Sunday).
#     Include both the start and end dates when counting.



# Waiting: 1. count_business_days("2026-02-24", "2026-02-26") should return 3.
# Waiting: 2. count_business_days("2026-02-24", "2026-02-28") should return 4.
# Waiting: 3. count_business_days("2026-02-21", "2026-03-01") should return 5.
# Waiting: 4. count_business_days("2026-03-08", "2026-03-17") should return 7.
# Waiting: 5. count_business_days("2026-02-24", "2027-02-24") should return 262.

from datetime import datetime, timedelta
def count_business_days(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    count = 0
    current = start_date
    while current <= end_date:
        if current.strftime("%A") not in ["Sunday", "Saturday"]:
            count += 1
        current += timedelta(days=1)
    return count

print(count_business_days("2026-02-24", "2026-02-26"))
print(count_business_days("2026-02-24", "2026-02-28"))
print(count_business_days("2026-02-21", "2026-03-01"))
print(count_business_days("2026-03-08", "2026-03-17"))
print(count_business_days("2026-02-24", "2027-02-24"))