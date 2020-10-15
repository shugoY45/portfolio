from datetime import datetime
from setting import *
from flask_schedule.models import Shift


def normal(workers,jobs):
  normalshifts = []
  # 時間を一定間隔に分割する
  opentime = datetime.strptime(store_opentime, '%H:%M')
  closetime = datetime.strptime(store_closetime, '%H:%M')
  for hour in range(opentime.hour,closetime.hour):
    one_shifts = []
    td_start = datetime.strptime(str(hour), '%H')
    td_end = datetime.strptime(str(hour+job_divtime), '%H')

    # 分割時間ごとの仕事の抽出
    td_jobs = []
    for job in jobs:
      start_time = datetime.strptime(job.starttime, '%H:%M')
      end_time = datetime.strptime(job.endtime, '%H:%M')
      if (start_time <= td_start and td_end <= end_time ):
        for i in range(0,int(job.required_number)):
          td_jobs.append(job)

    # 仕事の優先度ソート
    td_jobs = sorted(td_jobs,key=lambda x:int(x.priority),reverse=True)
    # print(td_jobs)


    # 仕事ごとに従業員を選定する
    for job in td_jobs:
      td_workers = []
      # print(job.jobname)
      for worker in workers:
        # 分割時間ごとの従業員の抽出
        if worker.be_free(td_start,td_end):
          td_workers.append(worker)
      # 仕事ごとに従業員を選定するため、人が一人ずつ仕事を振り分けられ減っていく
      if not len(td_workers) == 0:
        for worker in td_workers:
          worker.make_aptitude(td_start,td_end,job.jobname)
          # print(worker.workername,worker.aptitude)
        td_workers = sorted(td_workers,key=lambda x:int(x.aptitude))
        # print(td_workers)
        shift = Shift(td_workers[0].workername,job.jobname,td_start,td_end,job.priority)
        td_workers[0].add_shift(shift)
        normalshifts.append(shift)
      
  return normalshifts