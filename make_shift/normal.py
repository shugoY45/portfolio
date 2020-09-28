from datetime import datetime
from setting import *


def Normal(Worker,Job):
  one_shift = []
  # 時間を一時間ごとに分割する
  opentime = datetime.strptime(store_opentime, '%H:%M')
  closetime = datetime.strptime(store_closetime, '%H:%M')
  for hour in range(opentime.hour,closetime.hour):
    td_start = datetime.strptime(str(hour), '%H')
    td_end = datetime.strptime(str(hour+job_divtime), '%H')

    # 分割時間ごとの仕事の抽出
    td_job = []
    for job in Job:
      start_time = datetime.strptime(job[job_start_time], '%H:%M')
      end_time = datetime.strptime(job[job_end_time], '%H:%M')
      if (start_time <= td_start and end_time >= td_end ):
        for _ in range(0,int(job[required_number])):
          td_job.append(job)

    # 仕事の優先度ソート
    job_sorted = sorted(td_job,key=lambda x:int(x[priority]),reverse=True)
    # print(job_sorted)


    # 分割時間ごとの従業員の抽出
    td_worker = []
    for worker in Worker:
      start_time = datetime.strptime(worker[work_start_time], '%H:%M')
      end_time = datetime.strptime(worker[work_end_time], '%H:%M')
      if (start_time <= td_start and end_time >= td_end ):
        td_worker.append(worker)
    # 従業員の重み更新

    # 従業員の仕事の重みソート
    worker_sorted = sorted(td_worker,key=lambda x:int(x[work_weight]))


    # 仕事と従業員をマッチング
    
    i = 0
    # 仕事の量と従業員の人数を比較し場合分けする
    if len(worker_sorted) >= len(job_sorted):
      for _ in job_sorted:
        one_shift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M')))
        i += 1
    else:
      for _ in worker_sorted:
        one_shift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M')))
        i += 1
        
    # print(1)
    # print(str(hour) + "時台" + str(one_shift))
  
  return one_shift





