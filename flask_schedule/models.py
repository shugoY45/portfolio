from flask_schedule import db
from datetime import datetime, timedelta, time, date


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), nullable=False)
  position = db.Column(db.String(20))

  Sun = db.Column(db.Boolean)
  Sunstarttime = db.Column(db.Time)
  Sunendtime = db.Column(db.Time)
  Mon = db.Column(db.Boolean)
  Monstarttime = db.Column(db.Time)
  Monendtime = db.Column(db.Time)
  Tue = db.Column(db.Boolean)
  Tuestarttime = db.Column(db.Time)
  Tueendtime = db.Column(db.Time)
  Wed = db.Column(db.Boolean)
  Wedstarttime = db.Column(db.Time)
  Wedendtime = db.Column(db.Time)
  Thu = db.Column(db.Boolean)
  Thustarttime = db.Column(db.Time)
  Thuendtime = db.Column(db.Time)
  Fri = db.Column(db.Boolean)
  Fristarttime = db.Column(db.Time)
  Friendtime = db.Column(db.Time)
  Sat = db.Column(db.Boolean)
  Satstarttime = db.Column(db.Time)
  Satendtime = db.Column(db.Time)


  def __repr__(self):
    return f"Worker('{self.workername}', '{self.Sunstarttime}', '{self.Sunendtime}')"

  def init(self):
    self.starttime = "0:00"
    self.endtime = "0:00"

  

class Dayworker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  one_date = db.Column(db.DateTime, nullable=False)
  workername = db.Column(db.String(20), nullable=False)
  position = db.Column(db.String(20))
  starttime = db.Column(db.Time)
  endtime = db.Column(db.Time)

  def __repr__(self):
    return f"Dayworker('{self.one_date}','{self.workername}', '{self.starttime}', '{self.endtime}')"

  def shift_init(self,one_date):
    self.freetimeops = []
    self.freetimeeds = []
    self.starttime = datetime.combine(one_date,self.starttime)
    self.endtime = datetime.combine(one_date,self.endtime)
    self.d_st = self.starttime
    self.d_ed = self.endtime
    self.freetimeops.append(self.starttime)
    self.freetimeeds.append(self.endtime)
    self.indivshifts = []
    self.need_rest = False
    self.time_median = 0
    self.difference = 0
    self.done_reversed = False
    self.tmp_reststart = 0
    self.tmp_restend = 0
    self.aptitude = 0

  def be_free(self,shift_st,shift_ed):
    for op,ed in zip(self.freetimeops,self.freetimeeds):
      if op <= shift_st and shift_ed <= ed :
        return True
    return False


  def add_shift(self,shift):
    for op,ed in zip(self.freetimeops,self.freetimeeds):
      if op < shift.starttime and shift.endtime < ed :
        self.freetimeops.remove(op)
        self.freetimeeds.remove(ed)
        self.freetimeops.append(op)
        self.freetimeeds.append(shift.starttime)
        self.freetimeops.append(shift.endtime)
        self.freetimeeds.append(ed)
        break
      elif op == shift.starttime and shift.endtime < ed :
        self.freetimeops.remove(op)
        self.freetimeeds.remove(ed)
        self.freetimeops.append(shift.endtime)
        self.freetimeeds.append(ed)
      elif op < shift.starttime and shift.endtime == ed :
        self.freetimeops.remove(op)
        self.freetimeeds.remove(ed)
        self.freetimeops.append(op)
        self.freetimeeds.append(shift.starttime)
      elif op == shift.starttime and shift.endtime == ed :
        self.freetimeops.remove(op)
        self.freetimeeds.remove(ed)
    self.indivshifts.append(shift)
  
  def make_aptitude(self,td_start,td_end,jobname):
    self.aptitude = 0
    for shift in self.indivshifts:
      if td_end < shift.endtime:
        td = shift.endtime - td_end
        m,s = divmod(td.seconds,60)
        b = m
        td = shift.starttime - td_end
        m,s = divmod(td.seconds,60)
        a = m
      else:
        td = td_start - shift.starttime
        m,s = divmod(td.seconds,60)
        b = m
        td = td_start - shift.endtime
        m,s = divmod(td.seconds,60)
        a = m
      function = -b*b+1440*b+a*a-1440*a
      if jobname == shift.jobname:
        self.aptitude = self.aptitude + function * int(shift.jobweight) * 5
      else:
        self.aptitude = self.aptitude + function * int(shift.jobweight)


# class Weekday(db.Model):
#   weekday = db.Column(db.Integer,nullable=False)
#   starttime = db.Column(db.String(10))
#   endtime = db.Column(db.String(10))
#   worker_id = db.Column(db,Integer,db.ForeignKey('worker.id'),nullable=False)

#   def __repr__(self):
#     return f"Weekday('{self.weekday}','{self.starttime}','{self.endtime}','{self.worker_id}')"
  



class Shift(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  one_date = one_date = db.Column(db.DateTime, nullable=False)
  workername = db.Column(db.String(20), nullable=False)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.DateTime)
  endtime = db.Column(db.DateTime)
  jobweight = db.Column(db.Integer)
  priority = db.Column(db.String(3))
  position = db.Column(db.String(20))
  employee_priority = db.Column(db.String(3))
  parttime_priority = db.Column(db.String(3))
  helper_priority = db.Column(db.String(3))
  be_indispensable = db.Column(db.Boolean, default=False)


  def __init__(self,workername,jobname,starttime,endtime,jobweight,priority,workerposition,employee_priority,parttime_priority,helper_priority,be_indispensable):
    self.workername = workername
    self.jobname = jobname
    self.starttime = starttime
    self.veiwstarttime = starttime.strftime("%H:%M")
    self.endtime = endtime
    self.veiwendtime = endtime.strftime("%H:%M")
    self.jobweight = jobweight
    self.priority = priority
    self.workerposition = workerposition
    self.employee_priority = employee_priority
    self.parttime_priority = parttime_priority
    self.helper_priority = helper_priority
    self.be_indispensable = be_indispensable

  def __repr__(self):
    return f"Shift('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}','{self.jobweight}')"
    # return f"Shift('{self.workername}','{self.jobname}','{self.veiwstarttime}','{self.veiwendtime}','{self.jobweight}')"


  def remove(self):
    i = 1

  def transfer(self):
    i = 1


  




class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.Time)
  endtime = db.Column(db.Time)
  required_number = db.Column(db.Integer)
  priority = db.Column(db.String(3))
  weight= db.Column(db.String(3))
  
  employee_priority = db.Column(db.String(3))
  parttime_priority = db.Column(db.String(3))
  helper_priority = db.Column(db.String(3))
  be_indispensable = db.Column(db.Boolean, default=False)

  # jobtime = db.relationship('Jobtime', backref='job', lazy=True)
  # dayjob = db.relationship('Dayjob', backref='job', lazy=True)
  # everyday = db.Column(db.Boolean, default=False)
  # weekday = db.Column(db.Boolean, default=False)
  # monthday  = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f"Job('{self.jobname}','{self.starttime}','{self.endtime}')"

# class Jobtime(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   dayname = db.Column(db.String(5), nullable=False)
#   starttime = db.Column(db.Time)
#   endtime = db.Column(db.Time)
  # job_id = db.Column(db.Integer,db.ForeignKey('job.id'))

class Dayjob(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  one_date = db.Column(db.DateTime, nullable=False)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.Time)
  endtime = db.Column(db.Time)
  required_number = db.Column(db.Integer)
  priority = db.Column(db.String(3))
  weight= db.Column(db.String(3))
  
  employee_priority = db.Column(db.String(3))
  parttime_priority = db.Column(db.String(3))
  helper_priority = db.Column(db.String(3))
  be_indispensable = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f"DayJob('{self.jobname}','{self.starttime}','{self.endtime}')"



class SpecialJob(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20),nullable=False)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.Time)
  endtime = db.Column(db.Time)
  priority = db.Column(db.String(3))
  required_number = db.Column(db.Integer)

  def __repr__(self):
    return f"SpecialJob('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}')"

class Shiftconfig(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  store_opentime = db.Column(db.Time)
  store_closetime = db.Column(db.Time)
  job_divtime = db.Column(db.Time)
  min_shift = db.Column(db.Time)
  restnd_mint = db.Column(db.Time)
  resttime = db.Column(db.Time)
  restname = db.Column(db.String)
  priorty_max = db.Column(db.Integer)

  def init(self):

    # self.hourlist = []
    # self.minuteslist = ["00"]

    # for hour in range(int(self.store_opentime.hour),int(self.store_closetime.hour)+1):
    #   self.hourlist.append(hour)

    # # print(min_shift.minute)
    # if not self.min_shift.minute == 0:
    #   if 60 % float(self.min_shift.minute) == 0:
    #     div = 60 / float(self.min_shift.minute)
    #   for minutes in range(1,int(div)):
    #     self.minuteslist.append(minutes*int(self.min_shift.minute))

    # self.phour = int(self.min_shift.hour) if not int(self.min_shift.hour) == 0 else 1

    # self.pminute = int(self.min_shift.minute) if not int(self.min_shift.minute) == 0 else 60

    self.priorty_list = []
    for i in range(0,self.priorty_max):
      self.priorty_list.append(i)

  def timecombine(self,one_datetime):
    self.store_opentime = datetime.combine(one_datetime,self.store_opentime)
    self.store_closetime = datetime.combine(one_datetime,self.store_closetime)

class Position(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20))


class Test(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  test = db.Column(db.Time)
  jobtime = db.relationship('Test2', backref='test', lazy=True)

class Test2(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  test_id = db.Column(db.Integer,db.ForeignKey('test.id'))

