import datetime

a = datetime.datetime(year=2000,month=1,day=1,hour=12)
b = datetime.datetime(year=2000,month=1,day=1,hour=15)

c = a-b
d = datetime.timedelta(hours=1)

print(c>d)








  







