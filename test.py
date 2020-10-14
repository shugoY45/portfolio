
from flask_schedule import db
from flask_schedule.models import Worker,Shift
from datetime import datetime

workers = Worker.query.all()
for worker in workers:
  worker.init()


st = datetime.strptime("19:00","%H:%M")
ed = datetime.strptime("22:00","%H:%M")
shift = Shift("sasaki","reji",st,ed,10)
workers[0].add_shift(shift)
print(workers[0].workername,workers[0].be_free(st,ed),workers[0].freetimeops,workers[0].freetimeeds)






  







