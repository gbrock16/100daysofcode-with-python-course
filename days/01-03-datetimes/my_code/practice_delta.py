from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print(t)

print(t.days)

# only doing the seconds of the hours
print(t.seconds)

# how to get hours since no hours function:
hours = t.seconds / 60 / 60
print(hours)

eta = timedelta(hours=6)
today = datetime.today()

print('Today:', today)
print('ETA:', eta)

combo = today + eta
print('Addition:', combo)  # when in string form, time addition is formatted
