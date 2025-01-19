number1 = int(input(" enter with the first number "))
number2 = int(input(" enter with the second number "))
number3 = int(input(" enter with the third number "))
if (number1 > number2) and (number1 > number3) and (number2 > number3):
    print(" number1 is biggest ")
    print(" number3 is smallest ")
elif (number1 > number2) and (number1 > number3) and (number3 > number2):
    print(" number1 is biggest ")
    print(" number2 is smallest ")
elif (number2 > number1) and (number2 > number3) and (number3 > number1):
    print(" number2 is biggest ")
    print(" number1 is smallest ")
elif (number2 > number1) and (number2 > number3) and (number1 > number3):
    print(" number2 is biggest ")
    print(" number3 is smallest ")
elif (number3 > number1) and (number3 > number2) and (number1 > number2):
    print(" number3 is biggest ")
    print(" number2 is smallest ")
elif (number3 > number1) and (number3 > number2) and (number2 > number1):
    print(" number3 is biggest ")
    print(" number1 is smallest ")
