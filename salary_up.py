salary = float(input(" enter with your salary? "))
salary_up = 0
if (salary >0) and (salary < 280):
    salary_up = salary * 1.20
    print(" the salary before is ", salary)
    print(" the percentage after grown salary is ", 20)
    print(" how many gown your salary ", salary * 0.20)
    print(" the salary after grown is ", salary_up)
elif (salary >= 280) and (salary < 700):
    salary_up = salary * 1.15
    print(" the salary before is ", salary)
    print(" the percentage after grown salary is ", 15)
    print(" how many gown your salary ", salary * 0.15)
    print(" the salary after grown is ", salary_up)
elif (salary >= 700) and (salary < 1500):
    salary_up = salary * 1.10
    print(" the salary before is ", salary)
    print(" the percentage after grown salary is ", 10)
    print(" how many gown your salary ", salary * 0.10)
    print(" the salary after grown is ", salary_up)
elif (salary >= 1500):
    salary_up = salary * 1.05
    print(" the salary before is ", salary)
    print(" the percentage after grown salary is ", 5)
    print(" how many gown your salary ", salary * 0.05)
    print(" the salary after grown is ", salary_up)
else:
    print(" invalid salary")
