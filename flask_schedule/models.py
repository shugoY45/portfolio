from flask_schedule import db
from datetime import datetime, timedelta


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), nullable=False)
  Sunday = db.Column(db.Boolean)
  Sunstarttime = db.Column(db.String(10))
  Sunendtime = db.Column(db.String(10))
  Monday = db.Column(db.Boolean)
  Monstarttime = db.Column(db.String(10))
  Monendtime = db.Column(db.String(10))
  Tuesday = db.Column(db.Boolean)
  Tuestarttime = db.Column(db.String(10))
  Tueendtime = db.Column(db.String(10))
  Wednesday = db.Column(db.Boolean)
  Wedstarttime = db.Column(db.String(10))
  Wenendtime = db.Column(db.String(10))
  Thursday = db.Column(db.Boolean)
  Thustarttime = db.Column(db.String(10))
  Thuendtime = db.Column(db.String(10))
  Friday = db.Column(db.Boolean)
  Fristarttime = db.Column(db.String(10))
  Friendtime = db.Column(db.String(10))
  Saturday = db.Column(db.Boolean)
  Satstarttime = db.Column(db.String(10))
  Satendtime = db.Column(db.String(10))

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}')"

  def init(self):
    self.freetimeops = []
    self.freetimeeds = []
    self.d_st = datetime.strptime(self.starttime,"%H:%M")
    self.d_ed = datetime.strptime(self.endtime,"%H:%M")
    self.freetimeops.append(datetime.strptime(self.starttime,"%H:%M"))
    self.freetimeeds.append(datetime.strptime(self.endtime,"%H:%M"))
    self.indivshifts = []
    self.need_rest = False
    self.time_median = 0
    self.difference = 0
    self.done_reversed = False
    self.tmp_reststart = 0
    self.tmp_restend = 0
    self.aptitude = 0

  # def day_of_the_week(self):
  #   self.weekday = []
  #   if self.Sunday:
  #     self.weekday.append("日")
  #   if self.Sunday:
  #     self.weekday.append("月")
  #   if self.Sunday:
  #     self.weekday.append("火")
  #   if self.Sunday:
  #     self.weekday.append("水")
  #   if self.Sunday:
  #     self.weekday.append("木")
  #   if self.Sunday:
  #     self.weekday.append("金")
  #   if self.Sunday:
  #     self.weekday.append("土")
  #   day = ','.join(self.weekday)
  #   print(day)

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
    # print(self.indivshifts)






class Shift():

  def __init__(self,workername,jobname,starttime,endtime,jobweight):
    self.workername = workername
    self.jobname = jobname
    self.starttime = starttime
    self.veiwstarttime = starttime.strftime("%H:%M")
    self.endtime = endtime
    self.veiwendtime = endtime.strftime("%H:%M")
    self.jobweight = jobweight

  def __repr__(self):
    return f"Shift('{self.workername}','{self.jobname}','{self.veiwstarttime}','{self.veiwendtime}','{self.jobweight}')"
  # def __repr__(self):
  #   return f"Shift('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}','{self.jobweight}')"

  def remove(self):
    i = 1

  def transfer(self):
    i = 1


  




class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jobname = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  priority = db.Column(db.String(3))
  required_number = db.Column(db.Integer)

  def __repr__(self):
    return f"Job('{self.jobname}','{self.starttime}','{self.endtime}')"


class SpecialJob(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20),nullable=False)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  priority = db.Column(db.String(3))
  required_number = db.Column(db.Integer)

  def __repr__(self):
    return f"SpecialJob('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}')"
