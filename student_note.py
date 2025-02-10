note1 = float(input(" write first test? "))
note2 = float(input(" write second test? "))
note3 = float(input(" write third test? "))
media = (note1 + note2 + note3)/3
if (media >= 7) and (media < 10):
    print("student is approved")
elif (media >= 0) and (media < 7):
    print(" student is failed")
elif (media == 10):
    print("excellent, very good, congratulation")
else:
    print(" media incorrect")