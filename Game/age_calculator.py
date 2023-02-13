import datetime as dt

def ageCalculator(y, m, d):
    today = dt.datetime.now().date()
    convert = dt.date(y, m, d)
    age = int((today-convert).days / 365.25)
    print(age)

ageCalculator(2023, 2, 13)

