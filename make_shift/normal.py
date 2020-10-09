from datetime import datetime
from setting import *
from make_shift.function import WorkWeight, Classify


def Normal(Worker,Job,IndivShift):
  NormalShift = []
  # 時間を一時間ごとに分割する
  opentime = datetime.strptime(store_opentime, '%H:%M')
  closetime = datetime.strptime(store_closetime, '%H:%M')
  for hour in range(opentime.hour,closetime.hour):
    One_Shift = []
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
    job_sorted = sorted(td_job,key=lambda x:int(x[job_weight]),reverse=True)
    # print(job_sorted)


    # 分割時間ごとの従業員の抽出
    td_worker = []
    for worker in Worker:
      start_time = datetime.strptime(worker[work_start_time], '%H:%M')
      end_time = datetime.strptime(worker[work_end_time], '%H:%M')
      if (start_time <= td_start and end_time >= td_end ):
        td_worker.append(worker)
    # 従業員の重み更新
    td_worker = WorkWeight(td_worker,IndivShift,hour)

    # 従業員の仕事の重みソート
    worker_sorted = sorted(td_worker,key=lambda x:int(x[work_weight]))
    # print(worker_sorted)

    # 仕事と従業員をマッチング
    
    i = 0
    # 仕事の量と従業員の人数を比較し場合分けする
    if len(worker_sorted) >= len(job_sorted):
      for _ in job_sorted:
        NormalShift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
        One_Shift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
        i += 1
    else:
      for _ in worker_sorted:
        NormalShift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
        One_Shift.append((worker_sorted[i][worker_name],job_sorted[i][job_name],td_start.strftime('%H:%M'),td_end.strftime('%H:%M'),job_sorted[i][job_weight]))
        i += 1
        
    # print(1)
    # print(str(hour) + "時台" + str(One_Shift))
    IndivShift = Classify(One_Shift,IndivShift)
    # print(IndivShift)

  # print(IndivShift)
  return NormalShift





