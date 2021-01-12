from datetime import time,datetime,timedelta
import random
# from make_shift.normal import normal
# from make_shift.special import special
# from make_shift.rest import rest

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

def minimize(workers,jobs,spjobs,config):

  #山登り法を用いた最小化
  #スケジュールの点数を格納する
  opentime = config.store_opentime
  closetime = config.store_closetime
  hour_list = [i for i in range(opentime.hour,closetime.hour)]

  spshifts = special(workers,spjobs,config,hour_list)
  restshifts = rest(workers,config)

  for i in range(1):
    random.shuffle(hour_list)
    normalshifts = normal(workers,jobs,config)
    shifts = spshifts + restshifts + normalshifts
    # score = evaluation(shifts,workers)

  return minshifts

def evaluation(shifts,workers):
  score = 0
  for shift in shifts:
    score += int(shift.jobweight)
  return score

def similarity(indivshifts):
  return 1
