side1 = int(input(" what's the first side's triangle? "))
side2 = int(input(" what's with the second side's triangle? "))
side3 = int(input(" what's with the third side's triangle? "))
if (side1 + side2) > side3 or (side1 + side3) > side2 or (side2 + side3) > side1:
    print(" i's triangle")
    if (side1 == side2) and (side1 == side3):
        print(" it's triangle's equileteral ")
    elif ((side1 == side2) and (side1 != side3)) or ((side1 == side3) and (side1 != side2)) or ((side2 == side3) and (side2 != side1)):
        print(" it's isosceles")
    elif (side1 != side2) and (side1 != side3) and (side2 != side3):
        print(" it's triangle's scalene")
    else:
        print(" it isn't triangle ")