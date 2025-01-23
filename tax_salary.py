what_hour_work = float(input(" what is your hour's work? "))
how_many_hour_your_work = float(input(" how many hour you work this month? "))
salary = what_hour_work * how_many_hour_your_work
if (salary <= 900):
    union = salary * 0.03
    tax_eleven = salary * 0.11
    tax_salary = salary - (union + tax_eleven)
    print(" you have tax free")
elif (salary > 900) and (salary < 1500):
    tax_salary =
    print(" ")