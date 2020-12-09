from datetime import datetime
from flask_schedule.models import Shift,Job
from make_shift.function import make_one_shift

def special(workers,specialjobs,config):
  spshifts = []
  # 特別シフトの従業員を従業員リストから探索
  for spjob in specialjobs:
    spjobtojob = Job(
      jobname = spjob.jobname,
      priority = 100,
      weight= 100,
      employee_priority = 0,
      parttime_priority = 0,
      helper_priority = 0,
      be_indispensable = True
    )
    found = False
    for worker in workers:
      if spjob.workername == worker.workername:
        found = True
        # 特別シフト作成
        starttime = datetime.strptime(spjob.starttime, '%H:%M')
        endtime = datetime.strptime(spjob.endtime, '%H:%M')
        # if datetime.strptime(worker.starttime, '%H:%M')<=starttime and endtime<=datetime.strptime(worker.endtime, '%H:%M'):
        if worker.be_free(starttime,endtime):
          shift = make_one_shift(Shift,worker,spjobtojob,starttime,endtime)
          spshifts.append(shift)
          worker.add_shift(shift)

          # 特別シフトの時間を外し、従業員リストの仕事時間を更新する。
          # newworker = Worker(worker.workername,worker.starttime,spjob.starttime)
          # newworkers.append(newworker)
          # newworker = Worker(worker.workername,spjob.endtime,worker.endtime)
          # newworkers.append(newworker)
          # newworkers.remove(worker)
          break
        else :
          # print(worker)
          raise Exception(str(spjob.starttime)+'から'+str(spjob.endtime)+'の時間に'+str(worker.workername)+'さんはいません')
        

    if not found:
      print(spjob.workername)
      raise Exception('本日、'+str(spjob.workername)+'さんは出勤ではありません')

  # print(spshifts)
  # print(newworkers)

  return spshifts








