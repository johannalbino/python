import datetime 

t = datetime.time(4, 20, 1)

print(t.hour, ':', t.minute, ':', t.second, ':', t.microsecond)

print (datetime.time.min)
print (datetime.time.max)
print (datetime.time.resolution)

today = datetime.datetime.today()

print(today)

print(today.ctime())

print (today.resolution)

d1 = datetime.date(2019, 1, 1)
d2 = datetime.date(2019, 6, 17)

print (d2 - d1)


strdate = d1.strftime('%Y-%m-%d')

print (strdate.split('-'))