from datetime import time,datetime,timedelta

def ave_time(time_list):
  # time_list = (datetime,datetime, ...)
  time_sum = timedelta(hours=0,minutes=0)
  # 時刻部分のみを抽出しtimedeltaを作成
  zero = datetime.combine(time_list[0],time(hour=0))
  for i in time_list:
    td = i - zero
    time_sum = time_sum + td
  
  td = time_sum/len(time_list) # 平均

  # （経過）時間[sec] -> 時分秒
  h, m, s = td.seconds//3600, (td.seconds//60)%60, td.seconds%60
  ave = datetime.combine(time_list[0],time(hour=h,minute=m,second=s))
  return ave

def make_one_shift(Shift,worker,job,starttime,endtime):
  shift = Shift(worker.workername,job.jobname,starttime,endtime,job.priority,job.priority,worker.position,job.employee_priority,job.parttime_priority,job.helper_priority,job.be_indispensable)
  return shift

