
from datetime import time,date,datetime,timedelta


def ave_time(time_list):
  # time_list = (datetime,datetime, ...)
  time_sum = timedelta(hours=0,minutes=0)
  # 時刻部分のみを抽出しtimedeltaを作成
  zero = datetime.combine(time_list[0],time(hour=0))
  for i in time_list:
    td = i - zero
    time_sum = time_sum + td
  
  td = time_sum/len(time_list) # 平均

  # （経過）時間[sec] -> 時分秒
  h, m, s = td.seconds//3600, (td.seconds//60)%60, td.seconds%60
  ave = datetime.combine(time_list[0],time(hour=h,minute=m,second=s))
  return ave

a = time(hour=11,minute=10)
b = datetime(year=2020,month=10,day=10,hour=1,minute=0)
d=datetime(year=2020,month=10,day=10,hour=13,minute=0)
c = datetime.combine(b,a)

time_list = []
time_list.append(b)
time_list.append(d)
print(time_list)

z = ave_time(time_list)
print(z)
# zero = datetime.combine(b,time(hour=0))
# td1 = d-zero
# td2 = b-zero
# td = (td1 + td2)/2
# print(td)









  







