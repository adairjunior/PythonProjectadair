test1 = float(input(" enter with test1 "))
test2 = float(input(" enter with test2 "))
media = (test1 + test2)/2
if (media >= 7) and (media < 10):
    print(" you are approved")
elif (media >=0) and (media < 7):
    print(" you are rejected")
elif (media == 10):
    print(" you are fantastic")
else:
    print(" enter with test1 and test2 again")

