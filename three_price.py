price1 = float(input(" enter with the first price "))
price2 = float(input(" enter with the second price "))
price3 = float(input(" enter with the third price "))
if (price1 < price2) and (price1 < price3):
    print(" you will buy product 1")
elif (price2 < price1) and (price2 < price3):
    print(" you will buy product 2")
else:
    print(" you will buy product 3")