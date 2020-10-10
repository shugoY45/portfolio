from datetime import datetime
import copy
from setting import *
from make_shift.module import Shift,Worker

def special(workers,specialjobs):
  spshifts = []
  newworkers = copy.copy(workers)
  # 特別シフトの従業員を従業員リストから探索
  # print(workers)
  for spjob in specialjobs:
    found = False
    for worker in workers:
      if spjob.workername == worker.workername:
        found = True
        # 特別シフト作成
        starttime = datetime.strptime(spjob.starttime, '%H:%M')
        endtime = datetime.strptime(spjob.endtime, '%H:%M')
        if datetime.strptime(worker.starttime, '%H:%M')<=starttime and endtime<=datetime.strptime(worker.endtime, '%H:%M'):
          shift = Shift(worker.workername,spjob.jobname,spjob.starttime,spjob.endtime,spjob.priorty)
          spshifts.append(shift)

          # 特別シフトの時間を外し、従業員リストの仕事時間を更新する。
          newworker = Worker(worker.workername,worker.starttime,spjob.starttime)
          newworkers.append(newworker)
          newworker = Worker(worker.workername,spjob.endtime,worker.endtime)
          newworkers.append(newworker)
          newworkers.remove(worker)
          break
        else :
          # print(worker)
          raise Exception(str(spjob.starttime)+'から'+str(spjob.endtime)+'の時間に'+str(worker.workername)+'さんはいません')
        

    if not found:
      print(spjob.workername)
      raise Exception('本日、'+str(spjob.workername)+'さんは出勤ではありません')

  # print(spshifts)
  # print(newworkers)

  return newworkers,spshifts








