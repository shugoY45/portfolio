from datetime import datetime
import copy
from setting import *

def special(workers,specialjobs):
  spshifts = []
  newworkers = copy.copy(workers)
  # 特別シフトの従業員を従業員リストから探索
  # print(workers)
  for spjob in specialjobs:
    found = False
    for worker in workers:
      if spjob[spworker_name] == worker[worker_name]:
        found = True
        # 特別シフト作成
        starttime = datetime.strptime(spjob[spjob_start_time], '%H:%M')
        endtime = datetime.strptime(spjob[spjob_end_time], '%H:%M')
        if datetime.strptime(worker[work_start_time], '%H:%M')<=starttime and endtime<=datetime.strptime(worker[work_end_time], '%H:%M'):
          spshifts.append((worker[worker_name],spjob[spjob_name],spjob[spjob_start_time],spjob[spjob_end_time],spjob[spjob_weight]))

          # 特別シフトの時間を外し、従業員リストの仕事時間を更新する。
          newworkers.append((worker[worker_name],worker[work_start_time],spjob[spjob_start_time],0))
          newworkers.append((worker[worker_name],spjob[spjob_end_time],worker[work_end_time],0))
          newworkers.remove(worker)
          break
        # else :
          # print(worker)
          # raise Exception(str(spjob[spjob_start_time])+'から'+str(spjob[spjob_end_time])+'の時間に'+str(worker[worker_name])+'さんはいません')
        

    if not found:
      print(spjob[spworker_name])
      raise Exception('本日、'+str(spjob[spworker_name])+'さんは出勤ではありません')

  return newworkers,spshifts

  # print(spshifts)
  # print(newworkers)







