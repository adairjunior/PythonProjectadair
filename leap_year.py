year = int(input(" type the year? "))
if ((year % 400) == 0) or ((year % 4) == 0):
    print("this is leap year")
else:
    print(" don't leap year")