
class Shift:
  def __init__(self, workername, jobname, starttime, endtime, priorty):
    self.workername = workername
    self.jobname = jobname
    self.starttime = starttime
    self.endtime = endtime
    self.priorty = priorty
  def __repr__(self):
    return f"SpJob('{self.workername}'','{self.jobname}','{self.starttime}','{self.endtime}')"


class Worker:

  def __init__(self, workername,starttime,endtime):
    self.workername = workername
    self.starttime = starttime
    self.endtime = endtime
  workerweight = 0

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}', '{self.workerweight}')"

class Needrest(Worker):
  i = 1