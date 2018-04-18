from datetime import datetime
from datetime import date

today = datetime.today()

print(type(today))
print(today)

todaydate = date.today()

print(type(todaydate))
print(todaydate)

todaymonth = todaydate.month
todayday = todaydate.day
todayyear = todaydate.year

print('Month:', todaymonth)
print('Day:', todayday)
print('Year:', todayyear)

christmas = date(2018, 12, 25)

print(christmas - todaydate)

if christmas is not todaydate:
    print('Sorry there are still ' + str((christmas - todaydate).days) + ' days until Christmas!')
else:
    print('Yay it is Christmas!')
