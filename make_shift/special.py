from datetime import datetime
import copy
from setting import *

def Special(Worker,Specialjob):
  Spshift = []
  NewWorker = copy.copy(Worker)
  # 特別シフトの従業員を従業員リストから探索
  # print(Worker)
  for spjob in Specialjob:
    found = False
    for worker in Worker:
      if spjob[spworker_name] == worker[worker_name]:
        found = True
        # 特別シフト作成
        starttime = datetime.strptime(spjob[spjob_start_time], '%H:%M')
        endtime = datetime.strptime(spjob[spjob_end_time], '%H:%M')
        if datetime.strptime(worker[work_start_time], '%H:%M')<=starttime and endtime<=datetime.strptime(worker[work_end_time], '%H:%M'):
          Spshift.append((worker[worker_name],spjob[spjob_name],spjob[spjob_start_time],spjob[spjob_end_time]))

          # 特別シフトの時間を外し、従業員リストの仕事時間を更新する。
          NewWorker.append((worker[worker_name],worker[work_start_time],spjob[spjob_start_time],0))
          NewWorker.append((worker[worker_name],spjob[spjob_end_time],worker[work_end_time],0))
          NewWorker.remove(worker)
          break
        # else :
          # print(worker)
          # raise Exception(str(spjob[spjob_start_time])+'から'+str(spjob[spjob_end_time])+'の時間に'+str(worker[worker_name])+'さんはいません')
        

    if not found:
      print(spjob[spworker_name])
      raise Exception('本日、'+str(spjob[spworker_name])+'さんは出勤ではありません')

  return NewWorker,Spshift

  # print(Spshift)
  # print(NewWorker)







