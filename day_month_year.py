day = int(input(" type the day - dd? "))
month = int(input(" type the month - mm? "))
year = int(input(" type the year - yyyy? "))
if (day >= 1) and (day <= 31):
    if (month >= 1) and (month <= 12):
        print(" valid date")
        print(" The day is",day,". The month is", month,". The year is", year,". ")
    else:
        print(" invalid month")
else:
    print(" invalid date")
