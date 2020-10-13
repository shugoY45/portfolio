from flask_schedule import db
from datetime import datetime


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  workerweight = db.Column(db.String(3))
  freetimeops = []
  freetimeeds = []
  shifts = []
  need_rest = False
  time_median = 0
  differ_store_median = 0

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}', '{self.workerweight}')"

  def init_freetime(self):
    self.freetimeops = []
    self.freetimeeds = []
    self.freetimeops.append(datetime.strptime(self.starttime,"%H:%M"))
    self.freetimeeds.append(datetime.strptime(self.endtime,"%H:%M"))

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
      if op <= shift.starttime and shift.endtime <= ed :
        self.freetimeops.remove(op)
        self.freetimeeds.remove(ed)
        self.freetimeops.append(op)
        self.freetimeops.append(shift.starttime)
        self.freetimeeds.append(shift.endtime)
        self.freetimeeds.append(ed)
        break
    self.shifts.append(shift)



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
