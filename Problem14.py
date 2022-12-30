from datetime import date
f_date = date(1999, 2, 24)
l_date = date(2022, 12, 30)
delta = l_date - f_date
print(delta.days)