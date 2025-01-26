test1 = float(input(" enter with first test "))
test2 = float(input(" enter with the sencond test "))
media = (test1 + test2)/2
if (media >= 9) and (media <= 10):
    print(" student A")
    print(" you are approved")
    print(" the first test is ",test1)
    print(" the second test is ",test2)
    print(" the media is ", media)
elif (media >= 7.5) and (media < 9):
    print(" student B")
    print(" you are approved")
    print(" the first test is ", test1)
    print(" the second test is ", test2)
    print(" the media is ", media)
elif (media >= 6) and (media < 7.5):
    print(" student C")
    print(" you are approved")
    print(" the first test is ", test1)
    print(" the second test is ", test2)
    print(" the media is ", media)
elif (media >= 4) and (media < 6):
    print(" student D")
    print(" you failed")
    print(" the first test is ", test1)
    print(" the second test is ", test2)
    print(" the media is ", media)
elif (media < 4) and (media > 0):
    print(" student E")
    print(" you failed")
    print(" the first test is ", test1)
    print(" the second test is ", test2)
    print(" the media is ", media)
else:
    print(" invalid test")