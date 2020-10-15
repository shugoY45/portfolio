from datetime import datetime
from setting import *
# from make_shift.function import workweight, classify
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

    # # 分割時間ごとの従業員の抽出
    # td_workers = []
    # for worker in workers:
    #   if worker.free():
    #     td_workers.append(worker)

    # 仕事ごとに従業員を選定する
    for job in td_jobs:
      td_workers = []
      for worker in workers:
        if worker.be_free(td_start,td_end):
          td_workers.append(worker)
      if not len(td_workers) == 0:
        for worker in td_workers:
          worker.make_aptitude()
        td_workers = sorted(td_workers,key=lambda x:int(x.aptitude),reverse=True)
        shift = Shift(td_workers[0].workername,job.jobname,td_start,td_end,job.priority)
        td_workers[0].add_shift(shift)
        normalshifts.append(shift)
      


    
    # td_worker = []
    # for worker in workers:
    #   start_time = datetime.strptime(worker[work_start_time], '%H:%M')
    #   end_time = datetime.strptime(worker[work_end_time], '%H:%M')
    #   if (start_time <= td_start and end_time >= td_end ):
    #     td_worker.append(worker)
    # # 従業員の重み更新
    # td_worker = workweight(td_worker,indivshifts,hour)

    # # 従業員の仕事の重みソート
    # worker_sorted = sorted(td_worker,key=lambda x:int(x[work_weight]))
    # # print(worker_sorted)

    # # 仕事と従業員をマッチング
    
    # i = 0
    # # 仕事の量と従業員の人数を比較し場合分けする
    # if len(worker_sorted) >= len(job_sorted):
    #   for _ in job_sorted:
    #     normalshifts.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
    #     one_shifts.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
    #     i += 1
    # else:
    #   for _ in worker_sorted:
    #     normalshifts.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
    #     one_shifts.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
    #     i += 1
        
    # # print(1)
    # # print(str(hour) + "時台" + str(one_shifts))
    # indivshifts = classify(one_shifts,indivshifts)
    # # print(indivshifts)

  # print(indivshifts)
  return normalshifts