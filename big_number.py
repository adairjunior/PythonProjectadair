number1 = int(input(" enter with the first number "))
number2 = int(input(" enter with the second number "))
number3 = int(input(" enter with the third number "))
if ((number1 > number2)) and ((number1 > number3)):
    print(" number1 is biggest ")
elif ((number1 > number2) and (number3 > number1)):
    print(" number3 is biggest ")
else:
    print(" number2 is biggest ")