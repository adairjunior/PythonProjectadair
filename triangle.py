side1 = int(input(" what's the first side's triangle? "))
side2 = int(input(" what's with the second side's triangle? "))
side3 = int(input(" what's with the third side's triangle? "))
if (side1 + side2) > side3 or (side1 + side3) > side2 or (side2 + side3) > side1:
    print(" i's triangle")