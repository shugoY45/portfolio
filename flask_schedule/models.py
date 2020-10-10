from flask_schedule import db


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))
  workerweight = db.Column(db.String(3))

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}', '{self.workerweight}')"

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
