number1 = int(input(" enter with the first number "))
number2 = int(input(" enter with the second number "))
number3 = int(input(" enter with the third number "))
if (number1 > number2) and (number1 > number3) and (number2 > number3):
    print(" the order is ", number1, " ", number2, " ", number3)
elif (number1 > number2) and (number1 > number3) and (number3 > number2):
    print(" the order is ", number1," ", number3," ", number2)
elif (number2 > number1) and (number2 > number3) and (number1 > number3):
    print(" the order is ", number2, " ", number1, " ", number3)
elif (number2 > number1) and (number2 > number3) and (number3 > number1):
    print(" the order is ", number2," ", number3," ", number1)
elif (number3 > number1) and (number3 > number2) and (number1 > number2):
    print(" the order is ", number3, " ", number1, " ", number2)
elif (number3 > number1) and (number3 > number2) and (number2 > number1):
    print(" the order is ", number3," ", number2," ", number1)