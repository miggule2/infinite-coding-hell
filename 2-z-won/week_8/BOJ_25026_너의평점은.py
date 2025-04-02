TRIAL = 20
sum_of_credit = 0
sum_of_credit_times_grade = 0
dict_of_grade = {
    "A+":4.5,
    "A0":4.,
    "B+":3.5,
    "B0":3.,
    "C+":2.5,
    "C0":2.,
    "D+":1.5,
    "D0":1.,
    "F":0.
}
for _ in range(TRIAL):
    sub, credit, grade = map(str, input().split())
    if grade != "P":
        sum_of_credit += float(credit)
        sum_of_credit_times_grade += float(credit) * dict_of_grade[grade]

if sum_of_credit == 0: print(0)        
else: print(sum_of_credit_times_grade / sum_of_credit)