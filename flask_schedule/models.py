from flask_schedule import db
from datetime import datetime


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  workerweight = db.Column(db.String(3))

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}', '{self.workerweight}')"

  def init(self):
    self.freetimeops = []
    self.freetimeeds = []
    self.freetimeops.append(datetime.strptime(self.starttime,"%H:%M"))
    self.freetimeeds.append(datetime.strptime(self.endtime,"%H:%M"))
    self.indivshifts = []
    self.need_rest = False
    self.time_median = 0
    self.difference = 0
    self.done_reversed = False
    self.tmp_reststart = 0
    self.tmp_restend = 0

  def be_free(self,shift_st,shift_ed):
    for op,ed in zip(self.freetimeops,self.freetimeeds):
      if op <= shift_st and shift_ed <= ed :
        return True
    return False

  # def make_shifttime(self,shift_st,shift_ed):
  #   for op,ed in zip(self.freetimeops,self.freetimeeds):
  #     if op <= shift_st and shift_ed <= ed :
  #       self.freetimeops.remove(op)
  #       self.freetimeeds.remove(ed)
  #       self.freetimeops.append(op)
  #       self.freetimeops.append(shift_ed)
  #       self.freetimeeds.append(shift_st)
  #       self.freetimeeds.append(ed)
  #       break
  #   return 0
  
  # def make_shiftlist(self,min_time):
  #   pminutes = int(datetime.strptime(min_time,"%H:%M").minute) if not int(datetime.strptime(min_time,"%H:%M").minute) == 0 else 60
  #   self.shift = [[Shift() for i in range(int(60/pminutes))] for i in range(24)]


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
  
  def hello(self):
    print(self.workername,self.freetimeops)




class Shift():
  workername = 0
  jobname = 0
  starttime = 0
  endtime = 0
  jobweight = 0

  def __init__(self,workername,jobname,starttime,endtime,jobweight):
    self.workername = workername
    self.jobname = jobname
    self.starttime = starttime
    self.endtime = endtime
    self.jobweight = jobweight

  def __repr__(self):
    return f"Shift('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}','{self.jobweight}')"

  def remove(self):
    i = 1

  def transfer(self):
    i = 1


  




class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  jobname = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  priorty = db.Column(db.String(3))
  required_number = db.Column(db.Integer)

  def __repr__(self):
    return f"Job('{self.jobname}','{self.starttime}','{self.endtime}')"


class SpecialJob(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20),nullable=False)
  jobname = db.Column(db.String(20), nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  priorty = db.Column(db.String(3))
  required_number = db.Column(db.Integer)

  def __repr__(self):
    return f"SpecialJob('{self.workername}','{self.jobname}','{self.starttime}','{self.endtime}')"
