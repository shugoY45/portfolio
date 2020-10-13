from datetime import datetime
from flask_schedule import db
from flask_schedule.models import Worker
from setting import *
# class Worker():
  # workername = "yoshida"
  # starttime = "9:00"
  # endtime = "20:00"
  # freetimeop = []
  # freetimeed = []

  # def __init__(self,starttime,endtime):
  #   self.starttime = starttime
  #   self.endtime = endtime
  #   self.freetimeop.append(datetime.strptime(self.starttime,"%H:%M"))
  #   self.freetimeed.append(datetime.strptime(self.endtime,"%H:%M"))
  # def __repr__(self):
  #   return f"Worker('{self.workername}','{self.starttime}','{self.endtime}')"

# shugo = Worker("9:00","20:00")
# shugo.freetimeop.append(1)

# print(shugo.freetimeop)
# print(type(shugo.freetimeed))

workers = Worker.query.all()
for worker in workers:
  worker.init_freetime()
  st = datetime.strptime("10:00","%H:%M")
  ed = datetime.strptime("11:00","%H:%M")
  worker.make_shifttime(st,ed)
  # print([worker.freetimeop,worker.freetimeed])
  st = datetime.strptime("13:00","%H:%M")
  ed = datetime.strptime("14:00","%H:%M")
  worker.make_shifttime(st,ed)
  # print([worker.freetimeop,worker.freetimeed])
  # worker.make_shiftlist(min_shift)
  # worker.make_shift("yo",st,ed,2)
  # print(st.hour)
  

# print(workers[0].shift)
# workers[0].shift[0][0].jobname = "rezi"
# workers[0].shift[1][0].jobname = "job"

# print(workers[0].shift[0][0].jobname)





  







